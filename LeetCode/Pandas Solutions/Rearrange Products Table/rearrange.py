import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Melt the DataFrame to long format
    result = pd.melt(products, id_vars=['product_id'], 
                     value_vars=['store1', 'store2', 'store3'],
                     var_name='store', value_name='price')
    
    # Drop rows where price is null
    result = result.dropna(subset=['price'])
    
    # Convert the 'store' column values to match the desired format
    result['store'] = result['store'].str.replace('store', 'store')
    
    # Sort by product_id and store
    result = result.sort_values(by=['product_id', 'store']).reset_index(drop=True)
    
    return result

# Example usage
data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3'])
result = rearrange_products_table(products)
print(result)
