import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table to reorganize the data, making 'sale_date' the index, 'fruit' the columns, and 'sold_num' the values.
    sales_pivot = sales.pivot(index='sale_date', columns='fruit', values='sold_num')
    
    # Calculate the difference between the number of apples and oranges sold each day.
    # 'apples' and 'oranges' are now column names after the pivot.
    sales_pivot['diff'] = sales_pivot['apples'] - sales_pivot['oranges']
    
    # We're interested only in the 'sale_date' and 'diff' for the final output.
    result = sales_pivot[['diff']].reset_index()
    
    # The order by 'sale_date' should be maintained as it is the index. If not, we can sort the values.
    # result = result.sort_values('sale_date')
    
    return result
