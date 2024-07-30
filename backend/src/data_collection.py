import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_nba_data(player_id, season, rapidapi_key):
    url = f"https://api-nba-v1.p.rapidapi.com/players/statistics?id={player_id}&season={season}"
    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com'
    }
    try:
        logging.info(f"Fetching data for player {player_id} for season {season}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad response status
        data = response.json()
        logging.info(f"Response received: {data}")
        
        # Check if the response contains data
        if data['results'] == 0 or not data['response']:
            logging.warning("No game logs found")
            return None
        
        game_logs = data['response']
        columns = game_logs[0].keys()  
        df = pd.DataFrame(game_logs, columns=columns)
        df.to_csv(f'data/raw/player_{player_id}_season_{season}.csv', index=False)
        logging.info(f"Data saved to data/raw/player_{player_id}_season_{season}.csv")
        return df
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    player_id = '237'
    season = '2021'
    rapidapi_key = ''  
    fetch_nba_data(player_id, season, rapidapi_key)
