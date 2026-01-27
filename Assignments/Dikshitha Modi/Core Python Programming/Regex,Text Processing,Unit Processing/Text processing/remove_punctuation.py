# import re
# def remove_punctuation(data):
#     return re.sub(r'[!,-.?]',"",data)
# print(remove_punctuation("Wow!!! This is great... isn't it?"))

import string
def remove_punctuation(data):
    result=""
    for char in data:
        if char not in string.punctuation:
            result+=char
    return result
print(remove_punctuation("Wow!!! This is great... isn't it?"))