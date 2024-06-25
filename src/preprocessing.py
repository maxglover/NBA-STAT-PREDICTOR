import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    df = df.sort_values(by='GAME_DATE')
    df['RECENT_AVG_POINTS'] = df['PTS'].rolling(window=5).mean()
    df['HOME_AWAY'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)
    df.dropna(subset=['RECENT_AVG_POINTS'], inplace=True)
    df.to_csv(f'data/processed/processed_{file_path.split("/")[-1]}', index=False)
    return df

if __name__ == "__main__":
    preprocess_data('data/raw/player_201939_season_2022-23.csv')
