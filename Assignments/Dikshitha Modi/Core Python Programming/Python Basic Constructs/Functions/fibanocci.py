def generate_fibonacci(n):
    if n<=1:
        return n
    else:
        return generate_fibonacci(n-1)+generate_fibonacci(n-2)
result=[]
for i in range(6):
    result.append(generate_fibonacci(i))
print(result)
