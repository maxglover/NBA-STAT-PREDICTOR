import pandas as pd
import joblib

def predict_points(recent_avg_points, home_away, opponent_avg_points_allowed):
    model = joblib.load('model/model.joblib')
    new_game_data = pd.DataFrame({
        'RECENT_AVG_POINTS': [recent_avg_points],
        
    })
    predicted_points = model.predict(new_game_data)
    return predicted_points[0]

if __name__ == "__main__":
    predicted_points = predict_points(25.0, 1, 110.0)
    print(f'Predicted Points: {predicted_points}')
