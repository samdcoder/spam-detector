#make a dictionary
import os
import pickle
import json
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

def make_dict():
    dirc = "emails/"
    files = os.listdir(dirc)

    emails = [dirc + email for email in files]

    words = []
    c = 1
    for email in emails:
        f = open(email, encoding = 'latin-1')
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c += 1

    for i in range(len(words)):
        if not(words[i].isalpha()):
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

def make_dataset(dictionary):
    dirc = "emails/"
    files = os.listdir(dirc)

    emails = [dirc + email for email in files]

    feature_set = []
    labels = []

    c = 1
    for email in emails:
        data = []
        f = open(email, encoding = 'latin-1')
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))

        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(c)
        c += 1

    return feature_set, labels

d = make_dict()
features, labels = make_dataset(d)
x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)
clf = MultinomialNB()
clf.fit(x_train,y_train)

preds = clf.predict(x_test)

print(accuracy_score(y_test, preds))

#storing the model
filename = "spam-classifer.pkl"
model_pickle = open(filename, 'wb')
pickle.dump(clf, model_pickle)
model_pickle.close()

#storing the dictionary
with open('dictionary.json', 'w') as f:
    json.dump(d,f)
