import pandas as pd

json_data = {
    'data': [
        {'id': 1, 'name': 'John Doe'}, 
        {'id': 2, 'name': 'Jane Doe'}
    ]
}
df = pd.json_normalize(json_data, 'data')
print(df)
