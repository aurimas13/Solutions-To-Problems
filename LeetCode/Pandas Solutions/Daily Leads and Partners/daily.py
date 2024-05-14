import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by 'date_id' and 'make_name' and calculate unique counts for 'lead_id' and 'partner_id'
    result = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=pd.NamedAgg(column='lead_id', aggfunc='nunique'),
        unique_partners=pd.NamedAgg(column='partner_id', aggfunc='nunique')
    ).reset_index()

    return result

# Example usage
data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], 
        ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], 
        ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], 
        ['2020-12-7', 'honda', 2, 1]]
daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype(
    {'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})

# Get the number of distinct leads and partners
result = daily_leads_and_partners(daily_sales)
print(result)
