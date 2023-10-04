import pandas as pd

# Define the function
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
    # Sample Data
    data = [[101, 'Alice'], [102, 'Bob'], [103, 'Charlie']]
    customer = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype({'customer_id':'Int64', 'customer_name':'object'})
    data = [[1, '2020-03-01', 1500, 101, 1], [2, '2020-05-25', 2400, 102, 2], [3, '2019-05-25', 800, 101, 3], [4, '2020-09-13', 1000, 103, 2], [5, '2019-02-11', 700, 101, 2]]
    orders = pd.DataFrame(data, columns=['order_id', 'sale_date', 'order_cost', 'customer_id', 'seller_id']).astype({'order_id':'Int64', 'sale_date':'datetime64[ns]', 'order_cost':'Int64', 'customer_id':'Int64', 'seller_id':'Int64'})
    data = [[1, 'Daniel'], [2, 'Elizabeth'], [3, 'Frank']]
    seller = pd.DataFrame(data, columns=['seller_id', 'seller_name']).astype({'seller_id':'Int64', 'seller_name':'object'})

    # Test the function
    print(sellers_with_no_sales(customer, orders, seller))
    


