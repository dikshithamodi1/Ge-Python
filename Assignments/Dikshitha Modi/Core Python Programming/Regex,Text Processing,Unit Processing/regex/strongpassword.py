import re
pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$'
text="StrongP@ss1"
if re.match(pattern,text):
    print("strong")
else:
    print("not")