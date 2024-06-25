import os
import pandas as pd
from src.data_collection import fetch_nba_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.model_training import train_model
from src.prediction import predict_points
from dotenv import load_dotenv


load_dotenv('key.env')
rapidapi_key = os.getenv('rapidapi_key')


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    # Create necessary directories
    ensure_directory_exists('data/raw')
    ensure_directory_exists('data/processed')
    ensure_directory_exists('model')

    # Input from user
    player_id = input("Enter the player ID: ")
    season = input("Enter the season (e.g., 2022): ")
    recent_avg_points = float(input("Enter the recent average points: "))
    home_away = int(input("Enter 1 for home game or 0 for away game: "))
    opponent_avg_points_allowed = float(input("Enter the opponent's average points allowed: "))

    # Step 1: Data Collection
    print("Fetching data...")
    fetch_nba_data(player_id, season, rapidapi_key)
    
    # Step 2: Data Preprocessing
    raw_data_file = f'data/raw/player_{player_id}_season_{season}.csv'
    print("Preprocessing data...")
    preprocess_data(raw_data_file)
    
    # Step 3: Feature Engineering
    processed_data_file = f'data/processed/processed_player_{player_id}_season_{season}.csv'
    print("Creating features...")
    create_features(processed_data_file)
    
    # Step 4: Model Training
    features_data_file = f'data/processed/features_player_{player_id}_season_{season}.csv'
    print("Training model...")
    train_model(features_data_file)
    
    # Step 5: Prediction
    print("Making prediction...")
    predicted_points = predict_points(recent_avg_points, home_away, opponent_avg_points_allowed)
    print(f'Predicted Points: {predicted_points}')

if __name__ == "__main__":
    main()
