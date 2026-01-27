import json
def pretty_print(data):
    return json.dumps(data,indent=4)
data = {"user": {"name": "Alex", "age": 25, "city": "Mumbai"}}
print(pretty_print(data))
