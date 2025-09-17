import pandas as pd
json_data = {
    'user': {
        'id': 123,
        'info': {
            'name': 'John Doe',
            'email': 'john@example.com'
        },
        'roles': ['admin', 'user']
    }
}
df = pd.json_normalize(
    json_data,
    record_path=None,
    meta=[
        'user.id',
        ['user', 'info', 'name'],
        ['user', 'info', 'email'],
        'user.roles'
    ]
)
print(df)
