lis=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new=[]
for i in range(len(lis)):
    if i not in (0,4,5):
        new.append(lis[i])
print(new)
