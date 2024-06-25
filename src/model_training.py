import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_model(file_path):
    df = pd.read_csv(file_path)
    features = ['RECENT_AVG_POINTS', 'HOME_AWAY', 'OPPONENT_AVG_POINTS_ALLOWED']
    target = 'PTS'
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print(f'Root Mean Squared Error: {rmse}')
    joblib.dump(model, 'model/model.joblib')

if __name__ == "__main__":
    train_model('data/processed/features_player_201939_season_2022-23.csv')
