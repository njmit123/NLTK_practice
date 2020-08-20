import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

heartfulness_df = pd.read_csv('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/Participants - Virtual Heartfulness Feedback Form  (Responses).csv') 
# print(heartfulness_df) 
heartfulness_df = heartfulness_df.dropna() # dropped entries with empty feedback
# print(heartfulness_df['Feedback / Suggestion you would like to share with us.'])

heartfulness_df['Score'] = (0.5*heartfulness_df['How was the interaction with the trainer?'] + 0.3*heartfulness_df['How was the Heartfulness meditation experience?'] + 0.2*heartfulness_df['How smooth was the process?'])
# print(heartfulness_df['Score'])

cleaned_list = []

def clean_text(text):
    cleaned_text =''
    cleaned_list_final = []
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space 
    text = text.translate(translator)
    text = text.lower()
    for i in text:
        if i not in string.punctuation:
            cleaned_text+=i

    words = word_tokenize(cleaned_text)
    for i in words:
        if i not in set(stopwords.words('english')):
            cleaned_list_final.append(i)

    return cleaned_list_final

for i in heartfulness_df['Feedback / Suggestion you would like to share with us.']:
    cleaned_list.append(clean_text(i))
heartfulness_df['Emotions'] = ''
f = open('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/emotions.txt','r')
emotion_dict = {}

for line in f:
    clear_line = line.replace("\n",'').replace(",",'').replace("'",'')
    clear_line = clear_line.strip()
    word,emotion = clear_line.split(':')
    emotion_dict[word]=emotion
f.close()

for i in range(len(cleaned_list)):
    emotions = '#'
    for j in range(len(cleaned_list[i])):
        if cleaned_list[i][j] in emotion_dict.keys():
            emotions+=emotion_dict[cleaned_list[i][j]]
            emotions+="#"
    #print(emotions)
    heartfulness_df.at[i,"Emotions"] = emotions


heartfulness_df.to_csv('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/hearfulness_cleaned.csv')