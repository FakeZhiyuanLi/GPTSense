import os

import tensorflow as tf
from tensorflow.python import keras
from keras import layers
from keras import losses

tf.get_logger().setLevel('ERROR')

tfDatasetsPath = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "tfDatasets"))

trainDataset = tf.keras.utils.text_dataset_from_directory(os.path.join(tfDatasetsPath, "train"), batch_size=32, seed=1)
valDataset = tf.keras.utils.text_dataset_from_directory(os.path.join(tfDatasetsPath, "validation"), batch_size=32, seed=1)

encodeLayer = layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=250
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
