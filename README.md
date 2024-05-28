# Chess API Query and Data Analysis

This project is a personal initiative to create a Python script that queries a chess API to retrieve and analyze data about recent chess games played by a specific user. The script generates a summary report of the data.

## Features

- Queries the [Chess.com API](https://www.chess.com/news/view/published-data-api) to fetch recent chess games played by a given user.
- Retrieves data for the last 10 games played by the user.
- Calculates win, loss, and draw rates for the user.
- Identifies the most common opening move played by the user.
- Determines the average game duration (in moves) for the user.
- Generates a summary report with the analyzed data.

## Requirements

- Python 3.x
- `requests` library
- `python-chess` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ck-bit/chess-analysis.git
   cd chess-analysis
   ```

2. Install the required libraries:

   ```bash
   pip install requests
   pip install python-chess
   ```

## Usage

1. Replace the placeholder username with the actual Chess.com username you want to query in the script.

2. Run the script:

   ```bash
   python main.py
   ```

3. The script will output a summary report of the user's recent chess games, including:
   - Total number of games analyzed
   - Win, loss, and draw rates
   - Most common opening move
   - Average game duration
### Input

Replace the `user` variable in the script with the desired Chess.com username:

```python
user = "sample_user"
```

### Output

The script will print a summary report similar to the following:

```plaintext
Total number of games: 10
Win rate: 50.0%
Loss rate: 30.0%
Draw rate: 20.0%
Most common opening move: e4
Average game duration: 40 moves
```

## Code Structure

The main parts of the script are:

- `fetch_and_parse_monthly_archive(url)`: Fetches finished games given an API url for a specific month and year.
- `analyze_game_results(username)`: Calculates result rates for 10 most recent games.
- `calculate_avg_moves(username)`: Calculates average moves for 10 most recent games.
- `calculate_moves_per_game(game, board, player_color)`: Calculates the number of player's moves for one game.
- `most_common_opening(username)`: Calculates the most common opening for the player given 10 recent games.
- `main()`: wrapper function that fetches archives, aggregates statistics, and generates the report. 
- `generate_report(statistics)`: Generates and prints the summary report.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Chess.com](https://www.chess.com) for providing the API.
- This project uses the [python-chess](https://github.com/niklasf/python-chess) library for handling chess data.

---
