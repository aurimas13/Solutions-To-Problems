import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    # Ensure both content_id columns have the same type
    tv_program['content_id'] = tv_program['content_id'].astype(str)
    content['content_id'] = content['content_id'].astype(str)
    
    # Merge the tv_program and content DataFrames on content_id
    merged_df = pd.merge(tv_program, content, on='content_id')
    
    # Filter for kid-friendly movies in June 2020
    june_kid_movies = merged_df[(merged_df['Kids_content'] == 'Y') & 
                                (merged_df['content_type'] == 'Movies') &
                                (merged_df['program_date'] >= '2020-06-01') & 
                                (merged_df['program_date'] < '2020-07-01')]
    
    # Select distinct titles and rename the column to 'TITLE'
    distinct_titles = june_kid_movies[['title']].drop_duplicates()
    distinct_titles.columns = ['TITLE']
    
    return distinct_titles

# Example usage
data = [['2020-06-10 08:00', 1, 'LC-Channel'], ['2020-05-11 12:00', 2, 'LC-Channel'], ['2020-05-12 12:00', 3, 'LC-Channel'], 
        ['2020-05-13 14:00', 4, 'Disney Ch'], ['2020-06-18 14:00', 4, 'Disney Ch'], ['2020-07-15 16:00', 5, 'Disney Ch']]
tv_program = pd.DataFrame(data, columns=['program_date', 'content_id', 'channel']).astype(
    {'program_date':'datetime64[ns]', 'content_id':'Int64', 'channel':'object'})

data = [[1, 'Leetcode Movie', 'N', 'Movies'], [2, 'Alg. for Kids', 'Y', 'Series'], [3, 'Database Sols', 'N', 'Series'], 
        [4, 'Aladdin', 'Y', 'Movies'], [5, 'Cinderella', 'Y', 'Movies']]
content = pd.DataFrame(data, columns=['content_id', 'title', 'Kids_content', 'content_type']).astype(
    {'content_id':'object', 'title':'object', 'Kids_content':'object', 'content_type':'object'})

# Get the distinct titles of kid-friendly movies streamed in June 2020
result = friendly_movies(tv_program, content)
print(result)
