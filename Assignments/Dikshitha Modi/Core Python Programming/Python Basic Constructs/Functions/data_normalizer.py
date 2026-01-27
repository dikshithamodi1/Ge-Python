def data_normalizer(data):
    new=[]
    for s in data:
        s=s.strip()
        s=s.lower()
        new.append(s)
    print(new)
data=[" John ", "MARY", " Alex "]
data_normalizer(data)
