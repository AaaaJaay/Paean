punctuation = {'.', ',', '?', '!', '"', "'", ';', ':', '_'}

with open("alice.txt") as f:
    words = f.read().split()

with open("stopwords.txt") as f:
    stopwords = set(f.read().split()) 

def process(word):
    word = word.lower()
    while word[0] in punctuation:
        word = word[1:]
    while word[-1] in punctuation:
        word = word[:-1]
    return word

word_count = {}
for word in words:
    word = process(word)
    if word not in stopwords:
        word_count[word] = word_count.get(word, 0) + 1

counts = list(word_count.items())

def get_count(word_count):
    return word_count[1]

counts.sort(key=get_count, reverse=True)
print(counts[:3])
