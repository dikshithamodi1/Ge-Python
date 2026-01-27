def get_age(input_str):
    try:
        ans=int(input_str)
    except ValueError:
        return -1
print(get_age("twenty") )
