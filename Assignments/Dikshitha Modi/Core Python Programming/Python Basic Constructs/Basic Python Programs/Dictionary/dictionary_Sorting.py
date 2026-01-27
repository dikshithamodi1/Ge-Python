input_dict={"hari":3,"ram":7,"heer":5}
ans={}
for key,val in sorted(input_dict.items(),key=lambda item:item[1]):
    ans[key]=val
print("ascending order:",ans)
