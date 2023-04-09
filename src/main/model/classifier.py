import os
import sys

import tensorflow as tf
from tensorflow.python import keras
from keras import layers
from keras import losses
import trainClassifier

tf.get_logger().setLevel('ERROR')

GPTSensePath = os.path.abspath(os.path.join(__file__, "..", "..", "..", ".."))
weightsPath = os.path.join(GPTSensePath, "src", "main", "model", "weights")

trainDataset = tf.keras.utils.text_dataset_from_directory(os.path.join(GPTSensePath, "tfDatasets", "train"), batch_size=32, seed=1)

# 0 is chatGPT, 1 is human
def getTextFromDataset(text, label):
    return text

def preprocess(text, label):
    return encodeLayer(tf.expand_dims(text, -1)), label

encodeLayer = layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=250,
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
    model.load_weights(os.path.join(weightsPath, "model1"))
except:
    trainClassifier.train(weightsPath + "/", "model1", model, 10)
    try:
        model.load_weights(os.path.join(weightsPath, "model1"))
    except:
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
    # human response test
    print(predict("i love random things.my life is random. (well mostly). i don't know what's gonna happen in 5 seconds. it's all good. what shall i do 2morrow. hmmm. i have no f-cking clue. savory? see, that's random. just like the title. duh! nothing new i can tell u homies about my website so pack it. and i know my g/f and one of my friends reads this so i gotta have some control to it. and if i dont? (uhh. not going there). mmm! food! haha!")[0])