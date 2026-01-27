import re
def extract_urls(text):
    pattern=r'https?://\S+'
    urls=re.findall(pattern,text)
    return urls
print(extract_urls("Visit https://google.com and http://github.com"))