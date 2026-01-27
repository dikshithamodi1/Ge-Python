import json
def get_nested_value(json_data, key_path):
    try:
        current=json_data
        for key in key_path:
            current=current[key]
        return current
    except (KeyError,TypeError,IndexError):
        return None
data = {"company": {"department": {"employees": [{"name": "Riya", "id": 
101}]}}}
print(get_nested_value(data, ["company", "department", "employees", 0, 
"name"]))
