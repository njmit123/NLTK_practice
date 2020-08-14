import nltk
from nltk.corpus import wordnet

syns = wordnet.synsets("good")
# set of synonyms
print(syns)
print(syns[0].lemmas())
#printing only the names
print(syns[1].lemmas()[1].name())
# definition
print(syns[0].definition())
# example in sentence
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for i in syn.lemmas():
        synonyms.append(i.name())
        if(i.antonyms()):
            antonyms.append(i.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))