import json
contact = {"name": "Alex", "phone": "123-456-7890", "email": "alex@example.com"}
json_output=json.dumps(contact,indent=4,sort_keys=True)
print(json_output)
