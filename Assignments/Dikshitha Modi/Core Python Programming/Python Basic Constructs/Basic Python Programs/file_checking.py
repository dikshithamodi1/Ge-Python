import os
file_path="programs.txt"
if os.path.isfile(file_path):
    print("file exsits")
else:
    print("file doesn't exsits")
