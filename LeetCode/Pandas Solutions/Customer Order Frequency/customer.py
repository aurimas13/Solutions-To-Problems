import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge Orders with Product to calculate total spending
    orders_with_product = orders.merge(product, on='product_id')
    orders_with_product['total_spent'] = orders_with_product['price'] * orders_with_product['quantity']
    
    # Filter for June and July 2020
    june_orders = orders_with_product[(orders_with_product['order_date'] >= '2020-06-01') & 
                                      (orders_with_product['order_date'] <= '2020-06-30')]
    july_orders = orders_with_product[(orders_with_product['order_date'] >= '2020-07-01') & 
                                      (orders_with_product['order_date'] <= '2020-07-31')]
    
    # Group by customer_id and sum total spending
    june_spending = june_orders.groupby('customer_id')['total_spent'].sum().reset_index()
    july_spending = july_orders.groupby('customer_id')['total_spent'].sum().reset_index()
    
    # Filter customers who spent at least $100
    june_customers = june_spending[june_spending['total_spent'] >= 100]
    july_customers = july_spending[july_spending['total_spent'] >= 100]
    
    # Find customers who meet the criteria in both months
    qualifying_customers = pd.merge(june_customers, july_customers, on='customer_id', suffixes=('_june', '_july'))
    
    # Merge with customers to get names
    result = qualifying_customers.merge(customers, on='customer_id')[['customer_id', 'name']]
    
    return result

# Example usage
data = [[1, 'Winston', 'USA'], [2, 'Jonathan', 'Peru'], [3, 'Moustafa', 'Egypt']]
customers = pd.DataFrame(data, columns=['customer_id', 'name', 'country']).astype({'customer_id': 'Int64', 'name': 'object', 'country': 'object'})

data = [[10, 'LC Phone', 300], [20, 'LC T-Shirt', 10], [30, 'LC Book', 45], [40, 'LC Keychain', 2]]
product = pd.DataFrame(data, columns=['product_id', 'description', 'price']).astype({'product_id': 'Int64', 'description': 'object', 'price': 'Int64'})

data = [[1, 1, 10, '2020-06-10', 1], [2, 1, 20, '2020-07-01', 1], [3, 1, 30, '2020-07-08', 2], [4, 2, 10, '2020-06-15', 2], 
        [5, 2, 40, '2020-07-01', 10], [6, 3, 20, '2020-06-24', 2], [7, 3, 30, '2020-06-25', 2], [9, 3, 30, '2020-05-08', 3]]
orders = pd.DataFrame(data, columns=['order_id', 'customer_id', 'product_id', 'order_date', 'quantity']).astype(
    {'order_id': 'Int64', 'customer_id': 'Int64', 'product_id': 'Int64', 'order_date': 'datetime64[ns]', 'quantity': 'Int64'})

# Get customers who spent at least $100 in June and July 2020
result = customer_order_frequency(customers, product, orders)
print(result)
