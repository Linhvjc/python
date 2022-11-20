import random
import json
import pickle
import numpy as np
import csv
from t2s.text_to_speech import say
from time import strftime

import nltk
from nltk.stem import WordNetLemmatizer     #verify the same word

from tensorflow.python.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('./data/words.pkl', 'rb'))
classes = pickle.load(open('./data/classes.pkl', 'rb'))
model = load_model('./data/chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_word(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_word(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    
    results.sort(key = lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("Go! Bot is running")

while True:
    message = input("You: ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    time = strftime('%H:%M:%S:%p, Date: %d/%m/%Y')
    print("Bot: " + res)
    say(res)
    with open(r'./data/history.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([f'{message}', f'{res}', f'{time}'])