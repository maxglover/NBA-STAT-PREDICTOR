import pandas as pd

def preprocess_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in DataFrame:", df.columns)

        if 'points' not in df.columns:
            raise ValueError("Column 'PTS' not found in the DataFrame")

        #df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
        df = df.sort_values(by='game')

        if len(df) < 5:
            raise ValueError("Insufficient data: less than 5 rows")

        df['RECENT_AVG_POINTS'] = df['points'].rolling(window=5).mean()
        #df['HOME_AWAY'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)
        df.dropna(subset=['RECENT_AVG_POINTS'], inplace=True)

        output_file_path = f'data/processed/processed_{file_path.split("/")[-1]}'
        df.to_csv(output_file_path, index=False)
        print(f"Processed data saved to {output_file_path}")

        return df
    except Exception as e:
        print(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data('data/raw/player_201939_season_2022-23.csv')
