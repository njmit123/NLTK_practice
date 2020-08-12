from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "This is an example showing off stop word filtration"
words = word_tokenize(text)
filtered_words = []
stop_words = set(stopwords.words("english"))
for w in words:
    if w not in stop_words:
        filtered_words.append(w)

print(filtered_words)
