lis1=[1,2,3]
lis2=[4,5,1]
diff1=[i for i in lis1 if i not in lis2]
diff2=[i for i in lis2 if i not in lis1]
print("elements in lis1 not in lis2:",diff1)
print("elements in lis2 not in lis1:",diff2)
