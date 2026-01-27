from collections import Counter
def top_n_words(text,n):
    words=text.split()
    counts=Counter(words)
    return counts.most_common(n)
print(top_n_words("great service great product", 2))
