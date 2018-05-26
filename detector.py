#make a dictionary
import os
import pickle
import json
from collections import Counter

with open('dictionary.json') as f:
    d = json.load(f)

model_pickle = open('spam-classifer.pkl', 'rb')
clf = pickle.load(model_pickle)

while True:
    features = []
    inp = input(">").split()
    if inp == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    if res[0] == 0:
        print("Not Spam")
    else:
        print("Spam")
    #print ["Not Spam", "Spam!"][res[0]]
