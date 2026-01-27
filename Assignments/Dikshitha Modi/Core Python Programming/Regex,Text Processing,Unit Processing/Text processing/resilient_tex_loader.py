import unicodedata
def text_loader(filepath):
    encodings=["utf-8","latin-1"]
    for encoding in encodings:
        try:
            with open(filepath,"r",encoding=encoding) as file:
                text=file.read()
            break
        except Exception:
            text=None
    else:
        return []
    clened_lines=[]
    for line in text.splitlines():
        normalized=unicodedata.normalize("NFKD",line)
        cleaned="".join(
            char for char in normalized if not unicodedata.combining(char)
        )
        clened_lines.append(cleaned)
    return clened_lines
print(text_loader("input.txt"))