class Sentence:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


# Example usage:
sentence = Sentence("This is a simple sentence")
for word in sentence:
    print(word)
