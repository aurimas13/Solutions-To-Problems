import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by 'x' column
    point = point.sort_values(by='x')
    
    # Calculate the difference between consecutive points
    point['diff'] = point['x'].diff().abs()
    
    # Find the minimum distance (skip the first NaN value in the 'diff' column)
    shortest = point['diff'][1:].min()
    
    # Return the result as a DataFrame
    return pd.DataFrame({'shortest': [shortest]})

# Example usage
data = [[-1], [0], [2]]
point = pd.DataFrame(data, columns=['x']).astype({'x':'Int64'})
result = shortest_distance(point)
print(result)
