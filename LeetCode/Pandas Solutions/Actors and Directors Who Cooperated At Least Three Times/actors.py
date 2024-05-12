import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by 'actor_id' and 'director_id' and count the occurrences
    collaboration_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
    # Filter pairs with at least three collaborations
    frequent_collaborations = collaboration_counts[collaboration_counts['count'] >= 3]
    
    # Select only the 'actor_id' and 'director_id' columns
    result = frequent_collaborations[['actor_id', 'director_id']]
    
    return result

# Example usage
data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id': 'Int64', 'director_id': 'Int64', 'timestamp': 'Int64'})

# Get pairs with at least three collaborations
result = actors_and_directors(actor_director)
print(result)
