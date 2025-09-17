import json

n_json = '{"name": "Prajjwal", "age": 23, "address": {"city": "Prayagraj", "zipcode": "20210"}}'

data = json.loads(n_json)

name = data['name']
age = data['age']
city = data['address']['city']
zipc = data['address']['zipcode']

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Zipcode: {zipc}")
