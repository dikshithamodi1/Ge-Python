import re
def simple_pattern_check(string):
    pattern=r'\A[A-Z]'
    if re.match(pattern,string):
        print("String starts with capital letter")
    else:
        print("the starting letter is not capital")
simple_pattern_check("Python")
