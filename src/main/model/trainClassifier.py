import os

import tensorflow as tf
from tensorflow.python import keras
from keras import layers
from keras import losses

tf.get_logger().setLevel('ERROR')

trainDataset = tf.keras.utils.text_dataset_from_directory("/Users/zhiyuan/Desktop/Hackathon/GPTSense/tfDatasets/train", batch_size=32, seed=1)
valDataset = tf.keras.utils.text_dataset_from_directory("/Users/zhiyuan/Desktop/Hackathon/GPTSense/tfDatasets/validation", batch_size=32, seed=1)

encodeLayer = layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=250,
    # standardize='lower_and_strip_punctuation'
)

def getTextFromDataset(text, label):
    return text

def preprocess(text, label):
    return encodeLayer(tf.expand_dims(text, -1)), label

encodeLayer.adapt(trainDataset.map(getTextFromDataset))

vectorizedTrainDataset = trainDataset.map(preprocess)
vectorizedDevDataset = valDataset.map(preprocess)

def train(directory, modelName, model, epochs):
    if len(os.listdir(directory)) <= 1:
        model.fit(vectorizedTrainDataset, validation_data=vectorizedDevDataset, epochs=epochs)
        model.save_weights(directory + modelName)
        print("model saved to: " + directory + modelName)
    else:
        print("model already exists")