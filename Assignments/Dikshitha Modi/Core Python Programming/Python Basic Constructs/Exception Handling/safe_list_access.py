def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
print(get_item([10,20], 5) )
