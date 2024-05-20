import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    # Merge the employees and salaries dataframes on employee_id with an outer join
    merged_df = pd.merge(employees, salaries, on='employee_id', how='outer')
    
    # Filter rows where either name or salary is missing
    missing_info_df = merged_df[merged_df['name'].isna() | merged_df['salary'].isna()]
    
    # Select and sort the employee_id column
    result_df = missing_info_df[['employee_id']].sort_values(by='employee_id').reset_index(drop=True)
    
    return result_df

# Example usage
employees_data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
employees = pd.DataFrame(employees_data, columns=['employee_id', 'name']).astype({'employee_id': 'Int64', 'name': 'object'})
salaries_data = [[5, 76071], [1, 22517], [4, 63539]]
salaries = pd.DataFrame(salaries_data, columns=['employee_id', 'salary']).astype({'employee_id': 'Int64', 'salary': 'Int64'})

print(find_employees(employees, salaries))
