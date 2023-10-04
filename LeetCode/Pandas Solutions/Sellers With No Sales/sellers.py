import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter the Orders table for 2020 sales
    sales_2020 = orders[orders['sale_date'].dt.year == 2020]
    
    # Step 2: Identify the unique sellers who made sales in 2020
    sellers_with_sales_2020 = sales_2020['seller_id'].unique()
    
    # Step 3: Filter the Seller table to get sellers not in the above list
    result = seller[~seller['seller_id'].isin(sellers_with_sales_2020)]
    
    # Step 4: Order the result by seller_name in ascending order
    result = result.sort_values(by='seller_name').reset_index(drop=True)
    
    # Return only the seller_name column as per the problem statement
    return result[['seller_name']]

if __name__ == '__main__':
    customer = pd.DataFrame({'customer_id': [1, 2, 3, 4, 5], 'customer_name': ['Daniel', 'Elizabeth', 'Jules', 'Adam', 'Amelia']})
    orders = pd.DataFrame({'order_id': [1, 2, 3, 4, 5, 6, 7, 8], 'sale_date': ['2020-01-01', '2020-02-01', '2020-02-01', '2020-03-01', '2020-03-01', '2020-03-01', '2020-04-01', '2020-04-01'], 'customer_id': [1, 1, 2, 2, 2, 3, 4, 5], 'seller_id': [1, 2, 3, 1, 2, 3, 1, 1]})
    seller = pd.DataFrame({'seller_id': [1, 2, 3, 4, 5], 'seller_name': ['Daniel', 'Elizabeth', 'Jules', 'Adam', 'Amelia']})
    result = sellers_with_no_sales(customer, orders, seller)
    print(result)
    
    #   seller_name
    # 0        Adam
    # 1      Amelia
    # 2      Jules