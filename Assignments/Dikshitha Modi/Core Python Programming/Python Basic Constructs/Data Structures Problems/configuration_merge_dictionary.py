configuration_dict1={"timeout": 10}
configuration_dict2={"timeout": 20, "debug": True}
ans={**configuration_dict1,**configuration_dict2}#or can use update function
print(ans)
