import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # If orders is empty, return an empty DataFrame.
    if orders.empty:
        return pd.DataFrame({'customer_number': []})

    df = orders.groupby('customer_number').size().reset_index(name='count')
    df.sort_values(by='count', ascending = False, inplace=True)
    return df[['customer_number']][0:1]