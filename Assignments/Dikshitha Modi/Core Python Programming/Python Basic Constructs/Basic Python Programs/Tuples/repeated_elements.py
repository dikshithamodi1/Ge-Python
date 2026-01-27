tup=(1,2,3,1,5,3)
repeated_items=set([item for item in tup if tup.count(item)>1])
print(repeated_items)
