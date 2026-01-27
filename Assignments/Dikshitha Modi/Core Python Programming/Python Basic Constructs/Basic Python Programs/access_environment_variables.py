import os
print(os.environ.get('PATH'))
for key,value in os.environ.items():
    print(f"{key} = {value}")
