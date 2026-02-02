class CycleData:
    def __init__(self,data):
        if not data:
            raise ValueError
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        val=self.data[self.index]
        self.index=(self.index+1)% len(self.data)
        return val
    def reset(self):
        self.index=0
cycle=CycleData(["A","B","C"])
for val in cycle:
    print(val)