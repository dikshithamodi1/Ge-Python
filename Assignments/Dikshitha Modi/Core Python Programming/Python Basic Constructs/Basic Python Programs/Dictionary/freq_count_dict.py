string='w3resource'
freq_dict={}
for letter in string:
    if letter in freq_dict:
        freq_dict[letter]+=1
    else:
        freq_dict[letter]=1
print(freq_dict)
