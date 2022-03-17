# MLP for Pima Indians Dataset Serialize to JSON and HDF5
import json
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
from PIL import Image

from serum import dependency, inject


@dependency
@inject
class FileService:
    def __init(self):
        pass
    def prediction_results(self, image, filename):
        # resize and preprocess image
        # load machine learning model
        # save model pickle
        # input the image and predict
        # return the results in form of json
        # load json and create model
        labels = {1:'Bulging_Eyes', 2:'Crossed_Eyes', 3:'Glaucoma', 4:'Cataracts', 5:'Uveitis'}
        image = Image.open(f"Service/{filename}")
        image = tf.image.resize(image, (32, 32))
        with open('Service/model.json', 'r') as f:
            loaded_model_json = f.read()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("Service/model.h5")
        # evaluate loaded model on test data
        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        results = {}
        pr = loaded_model.predict(image[None])
        results['disease'] = labels[pr.argmax(axis=1)[0]]
        return results