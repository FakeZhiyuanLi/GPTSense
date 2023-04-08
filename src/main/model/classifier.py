import os
import sys

import tensorflow as tf
from tensorflow.python import keras
from keras import layers
from keras import losses

import trainClassifier

tf.get_logger().setLevel('ERROR')

trainDataset = tf.keras.utils.text_dataset_from_directory("/Users/zhiyuan/Desktop/Hackathon/GPTSense/tfDatasets/train", batch_size=32, seed=1)

def printLabels():
    print("Label 0 corresponds to", trainDataset.class_names[0])
    print("Label 1 corresponds to", trainDataset.class_names[1])


def getTextFromDataset(text, label):
    return text

def preprocess(text, label):
    return encodeLayer(tf.expand_dims(text, -1)), label

encodeLayer = layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=250,
    # standardize='lower_and_strip_punctuation'
)

encodeLayer.adapt(trainDataset.map(getTextFromDataset))

model = keras.Sequential([
    layers.Embedding(10001, 16),
    layers.Dropout(0.2),
    layers.GlobalAveragePooling1D(),
    layers.Dropout(0.2),
    layers.Dense(1)
])
model.compile(loss=losses.BinaryCrossentropy(from_logits=True), optimizer='adam', metrics=['accuracy'])

try:
    model.load_weights("/Users/zhiyuan/Desktop/Hackathon/GPTSense/src/main/model/weights/model1")
    print("using pretrained model")
except:
    print("retraining")
    trainClassifier.train("/Users/zhiyuan/Desktop/Hackathon/GPTSense/src/main/model/weights/", "model1", model, 10)
    try:
        model.load_weights("/Users/zhiyuan/Desktop/Hackathon/GPTSense/src/main/model/weights/model1")
    except:
        print("failed to retrain")
        sys.exit(0)

exportModel = keras.Sequential([
    encodeLayer,
    model,
    layers.Activation('sigmoid')
])
exportModel.compile(loss=losses.BinaryCrossentropy(from_logits=False), optimizer='adam', metrics=['accuracy'])

def predict(text):
    return exportModel.predict([text])[0]

if __name__ == '__main__':
    print(predict("i love random things.my life is random. (well mostly). i don't know what's gonna happen in 5 seconds. it's all good. what shall i do 2morrow. hmmm. i have no f-cking clue. savory? see, that's random. just like the title. duh! nothing new i can tell u homies about my website so pack it. and i know my g/f and one of my friends reads this so i gotta have some control to it. and if i dont? (uhh. not going there). mmm! food! haha!")[0])
    pass