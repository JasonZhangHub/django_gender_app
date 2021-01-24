from keras.models import load_model
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences

TOKENIZER_PATH = 'gender_recognition/tokenizer.pkl'
MODEL_PATH = 'gender_recognition/model.h5'

tokenizer = pickle.load(open(TOKENIZER_PATH, 'rb+'))

model = load_model(MODEL_PATH)


def seq(name):
    seq = tokenizer.texts_to_sequences(name)
    seq = [i[0] for i in seq]
    seq_list = []
    seq_list.append(seq)
    s = pad_sequences(seq_list, maxlen=15, padding='post')
    return s


def decoder(predicted):
    decode = np.argmax(predicted, axis=1)[0]
    return decode


def genderPredict(name):
    sequences = seq(name)
    predict = model.predict(sequences)
    result = decoder(predict)
    if result == 1:
        return("male")
    else:
        return("female")
