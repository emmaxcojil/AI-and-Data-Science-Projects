import random
import json
import pickle
import numpy as np
import nltk
import tensorflow as tf
from nltk.stem import WordNetLemmatizer


# After training the model, create the chatbot file

# create variable for lemmatizer
lemmatizer = WordNetLemmatizer()

# loading the files we made previously
# create variable, open and read in json file
intents = json.loads(open('intents.json').read())

# create variables for words and classes and use pickle to read in the files in binary mode
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# load model
model = tf.keras.models.load_model('chatbotmodel.h5')


# function to tokenize and lemmatize separate words in the input sentences
def clean_up_sentence(sentence):
    sentence_word = nltk.word_tokenize(sentence)
    sentence_word = [lemmatizer.lemmatize(word) for word in sentence_word]
    return sentence_word

# function to append 1 to a list variable ‘bag’ if the word is contained in input
def bag_of_words(sentence):
    sentence_word = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_word:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


# This function will predict the class of the sentence input by the user with an error threshold of 25%
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

        #print results for evaluation purposes
        print(f"class:{classes[r[0]]}, probability:{str(r[1])}")
        print(results)

    return return_list


# function to return random response from predicted class
def get_response(intents_list, intents_json):
    list_of_intents = intents_json['intents']
    tag = intents_list[0]['intent']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("Hello! Solent Support Bot at your service!")

# initialize infinite while loop to prompt the user and call functions
while True:
    message = input("Your message: ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(f"Solent Support bot: {res}")
    # Note: We have allowed predicted class and probability to display for project explanation purpose

