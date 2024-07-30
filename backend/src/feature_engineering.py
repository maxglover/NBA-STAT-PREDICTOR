import pandas as pd

def create_features(file_path):
    try:
        df = pd.read_csv(file_path)
        
        # Ensure 'MATCHUP' is not part of the index before grouping
        if 'MATCHUP' in df.index.names:
            df.reset_index(inplace=True)
        
        # Calculate the mean PTS per MATCHUP
        df['OPPONENT_AVG_POINTS_ALLOWED'] = df.groupby('MATCHUP')['PTS'].transform('mean')
        
        # Construct the output file path safely
        output_dir, output_file = os.path.split(file_path)
        processed_output_file = os.path.join(output_dir, f"features_{output_file}")
        
        # Save the modified DataFrame
        df.to_csv(processed_output_file, index=False)
        
        print(f"Features added and saved to {processed_output_file}")
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_features('data/processed/processed_player_201939_season_2022-23.csv')
