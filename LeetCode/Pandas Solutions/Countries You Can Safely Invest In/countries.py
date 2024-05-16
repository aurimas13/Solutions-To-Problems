import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    # Extract country code from phone_number in person DataFrame
    person['country_code'] = person['phone_number'].str[:3]
    
    # Merge calls with person to get caller and callee country codes
    calls_with_caller = calls.merge(person[['id', 'country_code']], left_on='caller_id', right_on='id', how='left').rename(columns={'country_code': 'caller_country_code'})
    calls_with_callee = calls.merge(person[['id', 'country_code']], left_on='callee_id', right_on='id', how='left').rename(columns={'country_code': 'callee_country_code'})
    
    # Combine the caller and callee data
    combined_calls = pd.concat([
        calls_with_caller[['duration', 'caller_country_code']].rename(columns={'caller_country_code': 'country_code'}),
        calls_with_callee[['duration', 'callee_country_code']].rename(columns={'callee_country_code': 'country_code'})
    ])
    
    # Calculate global average call duration
    global_avg_duration = combined_calls['duration'].mean()
    
    # Calculate average call duration for each country
    country_avg_durations = combined_calls.groupby('country_code')['duration'].mean().reset_index()
    
    # Merge with country data
    result = country_avg_durations.merge(country, left_on='country_code', right_on='country_code')
    
    # Filter countries where the average call duration is greater than the global average
    result = result[result['duration'] > global_avg_duration][['name']].rename(columns={'name': 'country'})
    
    return result

# Example usage
data = [[3, 'Jonathan', '051-1234567'], [12, 'Elvis', '051-7654321'], [1, 'Moncef', '212-1234567'], [2, 'Maroua', '212-6523651'], [7, 'Meir', '972-1234567'], [9, 'Rachel', '972-0011100']]
person = pd.DataFrame(data, columns=['id', 'name', 'phone_number']).astype({'id': 'Int64', 'name': 'object', 'phone_number': 'object'})

data = [['Peru', '051'], ['Israel', '972'], ['Morocco', '212'], ['Germany', '049'], ['Ethiopia', '251']]
country = pd.DataFrame(data, columns=['name', 'country_code']).astype({'name': 'object', 'country_code': 'object'})

data = [[1, 9, 33], [2, 9, 4], [1, 2, 59], [3, 12, 102], [3, 12, 330], [12, 3, 5], [7, 9, 13], [7, 1, 3], [9, 7, 1], [1, 7, 7]]
calls = pd.DataFrame(data, columns=['caller_id', 'callee_id', 'duration']).astype({'caller_id': 'Int64', 'callee_id': 'Int64', 'duration': 'Int64'})

# Get the countries where the company can invest
result = find_safe_countries(person, country, calls)
print(result)
