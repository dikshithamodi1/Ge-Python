def read_csv(filepath):
    with open(filepath,"r") as file:
        length=sum(1 for _ in file)
        return length
        