from flask import Flask, request, jsonify
from flask_cors import CORS
from src.data_collection import fetch_nba_data
from src.preprocessing import preprocess_data
from src.model_training import train_model
from src.prediction import predict_points
from dotenv import load_dotenv
import os
import logging

# Initialize the Flask app and configure CORS
app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv('key.env')
rapidapi_key = os.getenv('rapidapi_key')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log the request data
        logging.debug("Received request data: %s", request.json)
        
        data = request.json
        player_id = data['player_id']
        season = data['season']
        recent_avg_points = float(data['recent_avg_points'])
        home_away = int(data['home_away'])
        opponent_avg_points_allowed = float(data['opponent_avg_points_allowed'])

        # Step 1: Data Collection
        logging.debug("Fetching NBA data...")
        fetch_nba_data(player_id, season, rapidapi_key)

        # Step 2: Data Preprocessing
        raw_data_file = f'data/raw/player_{player_id}_season_{season}.csv'
        logging.debug("Preprocessing data...")
        preprocess_data(raw_data_file)

        # Step 3: Model Training
        processed_data_file = f'data/processed/processed_player_{player_id}_season_{season}.csv'
        logging.debug("Training model...")
        train_model(processed_data_file)

        # Step 4: Prediction
        logging.debug("Making prediction...")
        predicted_points = predict_points(recent_avg_points, home_away, opponent_avg_points_allowed)
        
        # Return the prediction result
        return jsonify({'predicted_points': predicted_points})
    except Exception as e:
        # Log the exception
        logging.error("An error occurred: %s", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
