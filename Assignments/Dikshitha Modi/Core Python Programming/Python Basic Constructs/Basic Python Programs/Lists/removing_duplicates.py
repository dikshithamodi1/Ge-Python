lis=[1,2,3,1,3,5,6]
new=[]
for i in lis:
    if i not in new:
        new.append(i)
print(new)
