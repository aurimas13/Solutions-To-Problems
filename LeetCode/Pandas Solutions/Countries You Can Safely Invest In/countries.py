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
    
    # Remove calls where country_code is NaN
    combined_calls = combined_calls.dropna(subset=['country_code'])
    
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
data = [[376, 'Gavriel', '078-6192794'], [369, 'Dalia', '637-0879945'], [130, 'Yaffah', '637-0126340'], [100, 'Naftali', '122-3190478'], [502, 'Gavriel', '870-5834859'], [426, 'Yehudit', '870-4713239']]
person = pd.DataFrame(data, columns=['id', 'name', 'phone_number']).astype({'id': 'Int64', 'name': 'object', 'phone_number': 'object'})

data = [['Brazil', '356'], ['Turkey', '379'], ['China', '078'], ['Israel', '120'], ['Algeria', '283'], ['Japan', '122']]
country = pd.DataFrame(data, columns=['name', 'country_code']).astype({'name': 'object', 'country_code': 'object'})

data = [[548, 13, 297], [801, 549, 265], [426, 368, 335], [948, 618, 543], [503, 426, 907], [217, 376, 631]]
calls = pd.DataFrame(data, columns=['caller_id', 'callee_id', 'duration']).astype({'caller_id': 'Int64', 'callee_id': 'Int64', 'duration': 'Int64'})

# Get the countries where the company can invest
result = find_safe_countries(person, country, calls)
print(result)
