import nltk
from nltk.corpus import state_union # data of USA Presidential speeches
from nltk.tokenize import PunktSentenceTokenizer # Creates an object trained on a training set to split text into sentences - we can train on training set
from nltk.tokenize import sent_tokenize # sentence tokenizer - pre trained
from nltk.tokenize import word_tokenize

train_text = state_union.raw("2005-GWBush.txt") # 2005 speech used to train
sample_text = state_union.raw("2006-GWBush.txt")

custom_model = PunktSentenceTokenizer(train_text) # custom_model trained on the 2005 speech
tokenized = custom_model.tokenize(sample_text) # tokenized is a sentence tokenized version of 2006 speech. Tokenization happens based on the training with 2005 speech

def pos_tagging():
    try:
        for i in tokenized:
            words=word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))

pos_tagging()
print("--------------------------------------------------------------------")
tokenized = sent_tokenize(sample_text)
pos_tagging()