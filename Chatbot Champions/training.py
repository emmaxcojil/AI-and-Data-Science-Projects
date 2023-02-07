import random
import json
import pickle
import numpy as np
import nltk
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,  Dropout
from keras.optimizers import SGD


# Create a WordNetLemmatizer() class object
# WordNetLemmatizer() gives the root words of the words that the Chatbot can recognize

# Read the contents from the “intents.json” file and store it to a variable “intents”
lemmatizer= WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

# empty lists are initialized to store the contents
words = []
classes = []
documents = []

# create variable for those characters to ignore
ignore_letters = ['?', '!', '.'',']

# use for loop to iterate through each intent sub-dictionary in intents file
for intent in intents['intents']:
    # iterate through patterns tokenize into word_list then add to words variable
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        # add the content to words
        words.extend(word_list)
        # create tuple of words_list and the tag and add to document variable - patterns with respective tags
        documents.append((word_list, intent['tag']))

        # appending the tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)

# storing the root words
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# create a set to remove duplicates and sort words to turn back into list
words = sorted(set(words))
print(words)

# create a set to remove duplicates and sort classes to turn back into list
classes = sorted(set(classes))

# saving the words and classes list to binary file using the pickle module’s dump() function
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Neural networks can only work with numerical values covert words to numbers - one hot encoding
# create an empty list called training, in which we’ll store the data used for training
training = []
# create an output_empty list that will store as many 0’s as there are classes in the intense.json
output_empty = [0]*len(classes)


# create bag of words - iterate through each word and append as either 1 if its already in bag or 0 if not
# (0, if the word isn’t in the pattern and 1 if the word is in the pattern)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    # making a copy of the output_empty
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    # add the bag and output_row to the training
    training.append([bag, output_row])

# shuffle this training set and make it a numpy array
random.shuffle(training)
training = np.array(training)

# Split the training set consisting of 1’s and 0’s into two parts, that is train_x and train_y
train_x = list(training[:,0])
train_y = list(training[:,1])

# create sequential ML neural network
model = Sequential()
# add layers input shape is same size as train_x, relu = rectified linear unit on first 2 layers
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# dropout layer to prevent over-fitting
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
# add output layer, same number of neurons as number of classes use softmax for activation
model.add(Dense(len(train_y[0]), activation='softmax'))


# stochastic gradient descent optimiser
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# compiling the model
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

print(model.summary())

# fit the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# saving the model
model.save('chatbotmodel.h5', hist)

# print statement to show that the Chatbot model has been trained successfully
print("Done: chatbot model has been trained successfully")
