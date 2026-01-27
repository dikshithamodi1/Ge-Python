def permute(lis,start):
    if len(lis)==start:
        print(lis)
    else:
        for i in range(start,len(lis)):
            lis[start],lis[i]=lis[i],lis[start]
            permute(lis,start+1)
            lis[start],lis[i]=lis[i],lis[start]
permute([1,2,3],0)
