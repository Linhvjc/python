import random
import json
import pickle       # for serialization
import numpy as np
import csv
import pandas as pd
from time import strftime

import nltk
from nltk.stem import WordNetLemmatizer     #verify the same word

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.optimizers import gradient_descent_v2

lemmatizer = WordNetLemmatizer()        #verify the same word

intents = json.loads(open('intents.json').read())       #Load file json

words = []          # All the words
classes = []        # All class 
documents = []
ignore_letters = ['?', '!', '.', ',']       # all ignore letters

def check_sentence_exist(sentence):
    df = pd.read_csv('./data/training_data.csv')
    
    for row in df.iterrows():
        if str(row[1]['Word list']) == str(sentence):
            return True
    return False

for intent in intents["intents"]:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)  # it look like split function ( 'what your name' => ['what', 'your','name'] )
        words.extend(word_list)     # add to array words
        documents.append((word_list, intent['tag']))   # add all word with tag to array documents
        if not check_sentence_exist(word_list):
            with open(r'./data/training_data.csv', 'a') as f:
                time = strftime('%H:%M:%S:%p, Date: %d/%m/%Y')
                writer = csv.writer(f)
                writer.writerow([f'{word_list}', f"{intent['tag']}", f'{time}'])
        if intent['tag'] not in classes:
            classes.append(intent['tag'])       # check if tag already have in classes and then add to array classes

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('./data/words.pkl', 'wb'))
pickle.dump(classes, open('./data/classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = gradient_descent_v2.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('./data/chatbot_model.h5', hist)
print("Done")

import tensorflow as tf
from tensorflow import keras

model_new = tf.keras.models.load_model("./data/chatbot_model.h5")
model_new.summary()
loss, acc = model_new.evaluate(train_x, train_y, verbose=1)
print('loss: ' + str(loss))
print('acc: ' + str(acc))

