from nltk.tokenize import sent_tokenize,word_tokenize
text="Hello there, how are you? I am Nilesh." # we would usually split by spaces for words and punctuation for sentences but cases like Mr.Smith can arise that are ambiguous
# NLTK solves these issues with ease as compared to using regexp
print(word_tokenize(text)) # split into words
print(sent_tokenize(text)) # split into sentences