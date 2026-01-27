import re

data = "Hi!! 😊 Alex#123"

# Replace all characters that are NOT letters, numbers, or spaces
cleaned_data = re.sub(r'[^a-zA-Z0-9 ]', '', data)

print(cleaned_data)
