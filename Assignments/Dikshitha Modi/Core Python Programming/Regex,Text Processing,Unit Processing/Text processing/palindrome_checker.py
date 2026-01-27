import string
def palindrome_checker(data):
    ans=""
    for s in data:
        if s not in string.punctuation and s!=" ":#s!= removes spaces
            ans+=s
    cleaned_data=ans.lower()
    print(cleaned_data==cleaned_data[::-1])
palindrome_checker("A man, a plan, a canal: Panama")