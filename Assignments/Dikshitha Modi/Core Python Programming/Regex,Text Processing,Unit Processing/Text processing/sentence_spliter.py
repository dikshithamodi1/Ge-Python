import re
def sentence_spliter(text):
    sentences=re.split(r'[?!.]',text)
    return [s.strip() for s in sentences if s.strip()]
print(sentence_spliter("Hi! How are you? I'm fine."))