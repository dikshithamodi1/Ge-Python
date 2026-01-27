def common(lis1,lis2):
    for i in lis1:
        if i in lis2:
            return True
    return False
lis1=[1,2,3]
lis2=[7,4,5]
print(common(lis1,lis2))
