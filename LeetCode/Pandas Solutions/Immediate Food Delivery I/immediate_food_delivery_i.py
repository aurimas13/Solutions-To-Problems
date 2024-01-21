import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    is_valid = delivery['order_date'] == delivery['customer_pref_delivery_date']
    
    # Count the number of valid (immediate) orders and the number of all orders.
    valid_count = is_valid.sum()
    total_count = len(delivery)

    # Round the percentage to 2 decimal places.
    percentage = round(100 * valid_count / total_count, 2)

    df = pd.DataFrame({'immediate_percentage': [percentage]})
    return df