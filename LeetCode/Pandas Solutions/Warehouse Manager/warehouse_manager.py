def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products['cubic_ft'] = products['Width'] * products['Height'] * products['Length']
    warehouse = warehouse.merge(
        products[['product_id', 'cubic_ft']], 
        how='left', 
        on='product_id'
        )
    warehouse['volume'] = warehouse['units'] * warehouse['cubic_ft']
    df = warehouse.groupby('name')['volume'].sum().reset_index(name="volume")

    # Rename 'name' to 'warehouse_name'
    df = df.rename(columns={'name':'warehouse_name'})
    
    return df