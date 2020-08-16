import nltk
from nltk.corpus import movie_reviews
import random

documents = [] # training set
documents = [(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
allwords = []
for w in movie_reviews.words():
    allwords.append(w.lower())
# lower case all words of all reviews added

allwords = nltk.FreqDist(allwords)
#print(allwords.most_common(15))
#print(allwords["stupid"])
# 3000 most common words
word_features = list(allwords.keys())[:3000]

def find_features(document):
    words = set(document) # all words in all reviews
    features = {} # boolean
    for w in word_features:
        features[w] = {w in words} # true or false depending on whether the word belongs to 3000 most commonly used words

    return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]
training_set = featuresets[:1900]
testing_set = featuresets[1900:]
classifier = nltk.NaiveBayesClassifier.train(training_set)
print('Accuracy of Naive Bayes algo : ', nltk.classify.accuracy(classifier,testing_set)*100)
classifier.show_most_informative_features(15)
