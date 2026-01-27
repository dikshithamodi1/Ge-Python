input_dict={"name":"hari","roll":2,"branch":"cse"}
keys_to_check=["name","roll","branch"]
all_exsist=all(key in input_dict for key in keys_to_check)
if all_exsist:
    print("all keys exsist")
else:
    print("multiple keys doesn't exsits")
