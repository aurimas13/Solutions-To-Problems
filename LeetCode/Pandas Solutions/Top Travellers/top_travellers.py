def top_travellers_updated(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # Group by user_id and sum the distance
    distance_sum = rides.groupby('user_id')['distance'].sum().reset_index()
    
    # Merge with users dataframe to get the names, using an outer join to include users without rides
    result = users.merge(distance_sum, how='left', left_on='id', right_on='user_id')[['name', 'distance']]
    
    # Fill NaN distances with 0 for users who haven't taken any rides
    result['distance'].fillna(0, inplace=True)
    
    # Rename the distance column to travelled_distance
    result.rename(columns={'distance': 'travelled_distance'}, inplace=True)
    
    # Sort the result by distance (descending) and name (ascending)
    result = result.sort_values(by=['travelled_distance', 'name'], ascending=[False, True]).reset_index(drop=True)
    
    return result

# Test the updated function with the provided data
if __name__ == '__main__':
    # Sample Data
    data = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
    users = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    data = [[1, 1, 10], [2, 1, 20], [3, 2, 15], [4, 2, 25], [5, 3, 30]]
    rides = pd.DataFrame(data, columns=['id', 'user_id', 'distance']).astype({'id':'Int64', 'user_id':'Int64', 'distance':'Int64'})

    # Test the function
    print(top_travellers(users, rides))
    
    #       name  travelled_distance
    # 0  Charlie                  30
    # 1      Bob                  40
    # 2    Alice                  30
