import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result

if __name__ == '__main__':
    person = pd.DataFrame({'personId': [1, 2, 3], 'firstName': ['John', 'Doe', 'Jane'], 'lastName': ['Doe', 'Black', 'Doe']})
    address = pd.DataFrame({'addressId': [1, 2, 3], 'personId': [1, 3, 2], 'city': ['Austin', 'Seattle', 'Austin'], 'state': ['TX', 'WA', 'TX']})
    result = combine_two_tables(person, address)
    print(result)
    
    #    firstName lastName     city state
    # 0      John      Doe   Austin    TX
    # 1       Doe    Black   Austin    TX
    # 2      Jane      Doe  Seattle    WA