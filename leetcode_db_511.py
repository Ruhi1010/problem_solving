import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by player_id and event_date
    activity = activity.sort_values(by=['player_id', 'event_date'])
    
    # Group by player_id and select the minimum event_date for each player
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return result

game_activity = pd.DataFrame({
    'player_id': [1, 2, 1, 3, 2, 1],
    'event_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-04', '2023-01-05']
})

result = game_analysis(game_activity)
print(result)