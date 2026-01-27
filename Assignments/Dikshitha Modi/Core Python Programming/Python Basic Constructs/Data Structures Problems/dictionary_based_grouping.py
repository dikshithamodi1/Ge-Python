from collections import defaultdict
data=[("IT", "Alex"), ("HR", "Riya"), ("IT", "John")]
dept_employees=defaultdict(list)
for key,value in data:
    dept_employees[key].append(value)
print(dict(dept_employees))
