import requests
from requests.exceptions import HTTPError
import chess.pgn 
from io import StringIO

num_games = 0
recent_games = []

def parse_month(url):
    # retreives up to 10 most recent games from a given month from an archive for a player
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        # Add other headers if needed (e.g., API key)
    }

  
    try: 
        response = requests.get(url, headers=headers)
        games = response.json()["games"]
        global recent_games
        global num_games
        for i in range(len(games) - 1, -1, -1):
            if num_games == 10: 
                break
            recent_games.append(games[i])
            num_games += 1

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")


def analyze_game_results(username):
    # iterates through list of games, calculates win, loss, and draw rates for a given user based on up to 10 recent games
    win, loss, draw = 0, 0, 0
    num_games = len(recent_games)
    for game in recent_games:
        if game["white"]["username"] == username:
            result = game["white"]["result"]
        else:
            result = game["black"]["result"]
        if result == "resigned" or result == "timeout":
            loss += 1
        elif result == "win":
            win += 1
        else:
            draw += 1
    return [win/num_games, loss/num_games, draw/num_games]

def calculate_avg_moves(username):
    moves_per_game = []
    for game in recent_games:
        player_color = "white" if game["white"]["username"] == username else "black"
        pgn_io = StringIO(game["pgn"])
        game = chess.pgn.read_game(pgn_io)
        board = game.board()
        moves_per_game.append(calculate_moves_per_game(game, board, player_color))
    return sum(moves_per_game) / len((moves_per_game)) 


def calculate_moves_per_game(game, board, player_color):
    white_moves = 0
    black_moves = 0
    for move in game.mainline_moves():
        
        if (board.turn):
            white_moves += 1
        if (not board.turn):
            black_moves +=1 
        board.push(move)
    return white_moves if player_color == "white" else black_moves
    
   

            
        # if player is white
    
def most_common_opening(username):
    pass


def generate_report(result_rates, avg_moves, common_opening, username):
    print(f"Generating report for user {username}...")
    print(f"Win rate for last 10 games: {result_rates[0] * 100}%")
    print(f"Loss rate for last 10 games: {result_rates[1] * 100}%")
    print(f"Draw rate for last 10 games: {result_rates[2] * 100}%")

    print(f"Average game duration (in moves): {avg_moves}")
    print(f"Most common opening move: no data yet.")


def main(): 
    username = "erik"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        # Add other headers if needed (e.g., API key)
    }

    url = f"https://api.chess.com/pub/player/{username}/games/archives"

    try:
        response  = requests.get(url, headers=headers)

        archive = response.json()
        months = archive["archives"]

        # traverse in reverse order starting from most recent month
        for i in range(len(months) - 1, -1, -1):
            if num_games == 10: break
            parse_month(months[i])

        result_rates = analyze_game_results(username)
        avg_moves = calculate_avg_moves(username)
        common_opening = most_common_opening(username)

        generate_report(result_rates, avg_moves, common_opening, username)





    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")


main()