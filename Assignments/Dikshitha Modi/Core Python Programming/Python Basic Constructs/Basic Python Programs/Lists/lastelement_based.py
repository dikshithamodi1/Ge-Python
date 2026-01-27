lis=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
new=[]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][-1]>lis[j][-1]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)
