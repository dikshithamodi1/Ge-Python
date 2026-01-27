import re
def safe_calculator(n,m):
    pattern =r'^-?\d+(\.\d+)$'
    if not re.match(pattern,n) and not re.match(pattern,m):
        return f"Error : Invalid Input Type"
    try:
        n=float(n)
        m=float(m)
        return n/m
    except ZeroDivisionError:
        return f"denominator can't be zero"
print(safe_calculator("10","a"))
