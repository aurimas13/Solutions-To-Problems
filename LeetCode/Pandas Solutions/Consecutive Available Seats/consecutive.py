import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter only the free seats and sort by seat_id
    df = cinema.query("free == 1")["seat_id"].sort_values()
    
    # Identify consecutive seats by checking if the difference is 1 for either forward or backward difference
    consecutive_seats = df.loc[(df.diff() == 1) | (df.diff(-1) == -1)]
    
    # Convert the result to a DataFrame
    return consecutive_seats.to_frame()

# Example usage
data = [[1, 1], [2, 0], [3, 1], [4, 1], [5, 1]]
cinema = pd.DataFrame(data, columns=['seat_id', 'free']).astype({'seat_id': 'Int64', 'free': 'int'})

result = consecutive_available_seats(cinema)
print(result)
