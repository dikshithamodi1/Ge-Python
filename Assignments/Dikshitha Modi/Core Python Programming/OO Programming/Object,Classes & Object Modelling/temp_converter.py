class Temperature:
    def to_farenheit(self,c):
        return (c*9/5) +32
    def to_celsius(self,f):
        return (f-32)*5/9
t=Temperature()
print(t.to_farenheit(0))
