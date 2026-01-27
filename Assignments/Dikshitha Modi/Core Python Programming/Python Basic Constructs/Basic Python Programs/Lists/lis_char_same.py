lis= ['abc', 'xyz', 'aba', '1221']
count=0
for s in lis:
    if len(s)>=2:
            if s[0]==s[-1]:
                count+=1
print(count)
