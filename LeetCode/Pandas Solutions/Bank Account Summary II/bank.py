import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # Group by 'account' and sum the 'amount'
    balance_df = transactions.groupby('account')['amount'].sum().reset_index()

    # Filter accounts with balance > 10000
    filtered_balance_df = balance_df[balance_df['amount'] > 10000]

    # Merge with users to get the 'name'
    result = pd.merge(filtered_balance_df, users, on='account')

    # Select relevant columns and rename them
    result = result[['name', 'amount']]
    result.columns = ['name', 'balance']

    return result

# Example usage
users_data = [[900001, 'Alice'], [900002, 'Bob'], [900003, 'Charlie']]
users = pd.DataFrame(users_data, columns=['account', 'name']).astype({'account': 'Int64', 'name': 'object'})

transactions_data = [[1, 900001, 7000, '2020-08-01'], [2, 900001, 7000, '2020-09-01'], 
                     [3, 900001, -3000, '2020-09-02'], [4, 900002, 1000, '2020-09-12'], 
                     [5, 900003, 6000, '2020-08-07'], [6, 900003, 6000, '2020-09-07'], 
                     [7, 900003, -4000, '2020-09-11']]
transactions = pd.DataFrame(transactions_data, columns=['trans_id', 'account', 'amount', 'transacted_on']).astype(
    {'trans_id': 'Int64', 'account': 'Int64', 'amount': 'Int64', 'transacted_on': 'datetime64[ns]'})

# Get the account summary
summary = account_summary(users, transactions)
print(summary)
