import re
def data_cleaner(text):
    pattern=r'^[a-zA-Z0-9]'
    try:
        cleaned = re.sub(r'[^a-zA-Z]', '', text)
        result = cleaned[4:]   # removes "Name"
        print(result)
    except:
        pass
data_cleaner("Na#me: A$le%x")