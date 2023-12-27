import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(orders, company, on='com_id')

    red_orders = df[df['name'] == 'RED']

    invalid_ids = red_orders.sales_id.unique()

    valid_sales_person = sales_person[~sales_person['sales_id'].isin(invalid_ids)]    

    return valid_sales_person[['name']]