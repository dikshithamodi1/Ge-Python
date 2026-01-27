def reverse_words(string):
    word=string.split(" ")
    reversed_s=""
    for s in word:
        reversed_s=reversed_s+" "+s[::-1]
    print(reversed_s)
string="Hello Python Developer"
reverse_words(string)
