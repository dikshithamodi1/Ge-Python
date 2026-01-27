data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_val=set()
for d in data:
    for val in d.values():#not data.values() bcoz that function only works for dictionary
        unique_val.add(val)
print(unique_val)
