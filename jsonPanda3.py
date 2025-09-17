import pandas as pd

json_data = {
    'company': 'Example Corp', 
    'employees': [
        {
            'id': 1, 
            'name': 'John Doe', 
            'positions': [
                {'title': 'CEO', 'years': 5}, 
                {'title': 'CTO', 'years': 3}
            ]
        }, 
        {
            'id': 2, 
            'name': 'Jane Doe', 
            'positions': [
                {'title': 'CFO', 'years': 4}, 
                {'title': 'CMO', 'years': 2}
            ]
        }
    ]
}

df = pd.json_normalize(
    json_data, 
    record_path=['employees', 'positions'], 
    meta=[
        ['employees', 'id'], 
        ['employees', 'name']
    ]
)
print(df)
