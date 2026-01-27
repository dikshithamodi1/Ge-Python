data={"name":"dikshitha","roll":34,"branch":"cse"}
print("{:<15} {:<15}".format("Key","Value"))
print("-"*30)
#< is used for left aligned and format is also used for aligning
for key,val in data.items():
    print("{:<15} {:<15}".format(key,val))
