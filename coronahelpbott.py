#Advanced Python Project 10: Corona Help Bot 
#json file: World Health Organization 
import nltk 
import random 
import json 
import pickle 

from nltk.stem.lancaster import LancasterStemmer 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.linear_model import LogisticRegression

stemmer = LancasterStemmer()

#Load Data 
with open("WHO.json") as file:
    data = json.load(file)
    
sentences = []
labels = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])
    tags.append(intent["tag"])
    
#Convert text to numbers 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

#Train model 

model = LogisticRegression()
model.fit(X, labels)

#Chat function 

def chat():
    print("Start chatting (type quit to stop)")
    
    while True:
        inp = input("You:")
        if inp.lower() == "quit":
            break 
        
        X_test = vectorizer.transform([inp])
        tag = model.predict(X_test)[0]
        
        for intent in data["intents"]:
            if intent["tag"] == tag:
                print(random.choice(intent["responses"]))
chat()