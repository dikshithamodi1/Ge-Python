from collections import defaultdict
grouped=defaultdict(list)
words=["apple","banana","apricot","cherry","blueberry"]
for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))
