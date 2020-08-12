from nltk import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

ps = PorterStemmer()
text = ["kicked","kicking","kick","kicker"]
for w in text:
    print(ps.stem(w))

# example with a sentence
print("\n")
sample = "Hello I kicked my friend yesterday, when he was kicking my football. I think the kick ended up being too hard"
sample_words = word_tokenize(sample)
stop_words = set(stopwords.words("english"))
filtered_words = []
for s in sample_words:
    if s not in stop_words:
        filtered_words.append(s)
for s in filtered_words:
    print(ps.stem(s))
