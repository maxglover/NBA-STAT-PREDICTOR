import pandas as pd

def create_features(file_path):
    df = pd.read_csv(file_path)
    # Placeholder: Example feature, actual opponent data needed
    df['OPPONENT_AVG_POINTS_ALLOWED'] = df.groupby('MATCHUP')['PTS'].transform('mean')
    df.to_csv(f'data/processed/features_{file_path.split("/")[-1]}', index=False)
    return df

if __name__ == "__main__":
    create_features('data/processed/processed_player_201939_season_2022-23.csv')
