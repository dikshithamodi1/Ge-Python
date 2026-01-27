lis=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_res=[]
for s in lis:
    if s not in new_res:
        new_res.append(s)
print(new_res)
