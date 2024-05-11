import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by 'email' and count occurrences
    email_counts = person.groupby('email').size().reset_index(name='count')
    
    # Filter emails that appear more than once
    duplicates = email_counts[email_counts['count'] > 1]
    
    # Select only the 'email' column
    result = duplicates[['email']]
    
    return result

# Example usage
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'Int64', 'email': 'object'})

# Get duplicate emails
duplicate_emails_result = duplicate_emails(person)
print(duplicate_emails_result)
