import re

text = "Card: 1234-5678-9012-3456"
pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'  # match the card number
ans = re.sub(pattern, "****-****-****-****", text)
print(ans)
