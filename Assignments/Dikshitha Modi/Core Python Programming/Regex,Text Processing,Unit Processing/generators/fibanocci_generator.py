def fibanooci(a,b,n):
    count=0
    while count<n:
        yield a
        a,b=b,a+b
        count+=1

f=fibanooci(0,1,10)
for val in f:
    print(val)