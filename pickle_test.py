import pickle

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
s1 = student("Ram",21)
s2 = student('Mayank', 20)
s3 = student('Shubham',35)
f1 = open("/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/test_pickle.txt","rb")
#1 = (s1,s2,s3)
#pickle.dump(t1,f1)
t1 = pickle.load(f1)
for i in t1:
    print(i.name)
f1.close()

