import json
json_string = '{"product": "Laptop", "price": 899.99, "in_stock": true}'
data=json.loads(json_string)
print(data["price"])
