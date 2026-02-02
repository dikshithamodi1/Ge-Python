class Numbers:
    def __init__(self, n):
        self.n = n
        self.current = 1  # start counting from 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        num = self.current
        self.current += 1
        return num


# Example usage:
no = Numbers(5)
for val in no:
    print(val)
