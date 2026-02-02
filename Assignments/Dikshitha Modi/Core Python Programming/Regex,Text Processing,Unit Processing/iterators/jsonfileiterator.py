import json
class JSONFileIterator:
    def __init__(self,filename):
        self.filename=filename
        self.file=open(filename,"r")
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            line=self.file.readline()
            if not line:#EOF
                self.file.close()
                raise StopIteration
            line=line.strip()
            if not line:#empty lines
                continue
            try:
                record = json.loads(line)  # parse JSON
                return record
            except json.JSONDecodeError:
                # Log or skip the malformed line, continue to next line
                print(f"Skipping malformed JSON: {line}")
                continue
for record in JSONFileIterator("huge_file.json"):
    print(record)

