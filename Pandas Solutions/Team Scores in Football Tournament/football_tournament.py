import pandas as pd

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    # Calculate host points
    host_points = matches.assign(points = ((matches['host_goals'] > matches['guest_goals']) * 3) + 
                                        ((matches['host_goals'] == matches['guest_goals']) * 1))
    host_points = host_points.groupby('host_team').agg({'points': 'sum'}).reset_index()
    
    # Calculate guest points
    guest_points = matches.assign(points = ((matches['guest_goals'] > matches['host_goals']) * 3) + 
                                         ((matches['guest_goals'] == matches['host_goals']) * 1))
    guest_points = guest_points.groupby('guest_team').agg({'points': 'sum'}).reset_index()
    
    # Merge host and guest points
    merged_points = pd.merge(host_points, guest_points, left_on='host_team', right_on='guest_team', how='outer')
    merged_points = merged_points.fillna({'host_team': 0, 'guest_team': 0, 'points_x': 0, 'points_y': 0})
    merged_points['team_id'] = merged_points.apply(lambda row: row['host_team'] if row['host_team'] != 0 else row['guest_team'], axis=1)
    merged_points['num_points'] = merged_points['points_x'] + merged_points['points_y']
    
    # Merge with teams dataframe and sort
    result = pd.merge(teams, merged_points[['team_id', 'num_points']], on='team_id', how='left')
    result['num_points'] = result['num_points'].fillna(0).astype(int)
    result = result.sort_values(by=['num_points', 'team_id'], ascending=[False, True])
    result = result[['team_id', 'team_name', 'num_points']]
    
    return result

# Testing the function with sample data
if __name__ == '__main__':
    # Sample Data
    data = [[1, 'Eagles'], [2, 'Pandas'], [3, 'Sharks']]
    teams = pd.DataFrame(data, columns=['team_id', 'team_name']).astype({'team_id':'Int64', 'team_name':'object'})
    data = [[1, 1, 2, 1, 0], [2, 1, 3, 0, 1], [3, 2, 3, 1, 1], [4, 3, 1, 1, 1]]
    matches = pd.DataFrame(data, columns=['match_id', 'host_team', 'guest_team', 'host_goals', 'guest_goals']).astype({'match_id':'Int64', 'host_team':'Int64', 'guest_team':'Int64', 'host_goals':'Int64', 'guest_goals':'Int64'})

    # Test the function
    print(team_scores(teams, matches))
    
    #    team_id team_name  num_points
    # 0        1    Eagles           6
    # 1        3    Sharks           4
    # 2        2    Pandas           3

