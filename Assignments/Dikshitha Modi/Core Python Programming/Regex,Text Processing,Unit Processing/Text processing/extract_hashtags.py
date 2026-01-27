def extract_hastags(text):
    ans=[]
    for s in text.split():
        if s.startswith("#"):
            ans.append(s)
    return ans
print(extract_hastags("Learning #Python and #DataScience today!"))