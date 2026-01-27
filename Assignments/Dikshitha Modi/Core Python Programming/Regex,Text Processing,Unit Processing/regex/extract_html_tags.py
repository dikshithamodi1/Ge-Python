import re
def extract_html_tags(text):
    pattern=r'</?([a-zA-Z]+)'
    tags=re.findall(pattern,text)
    unique=list(set(tags))
    print(unique)
extract_html_tags("<div><a href='#'>Link</a></div>")