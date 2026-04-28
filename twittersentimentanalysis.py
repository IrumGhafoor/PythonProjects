#Advanced Python Project 2: Twitter Sentiment Analysis

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression 
from sklearn.svm import LinearSVC 
from sklearn.metrics import accuracy_score, classification_report

#Load Dataset 
df = pd.read_csv('archive (1).zip', encoding = 'latin-1', header=None)
df = df[[0, 5]]
df.columns = ['polarity', 'text']
print(df.head())

#Keep only positive and negative sentiments
df = df[df.polarity != 2]

df['polarity'] = df['polarity'].map({0: 0, 4:1})
print(df['polarity'].value_counts())

#Clean the Tweets
def clean_text(text):
    return text.lower()
df['clean_text'] = df['text'].apply(clean_text)

print(df[['text', 'clean_text']].head())

#Train Test Split 
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'],
    df['polarity'],
    test_size = 0.2,
    random_state = 42
)
print("Train size:", len(X_train))
print("Test size:", len(X_test))

#Perform Vectorization 

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("TF-IDF shape (train):", X_train_tfidf.shape)
print("TF-IDF shape (test):", X_test_tfidf.shape)
