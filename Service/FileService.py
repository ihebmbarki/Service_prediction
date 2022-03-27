#TensorFlow trains and runs deep neural networks for handwritten digit classification
# image recognition in this case
import tensorflow as tf
# The Python Imaging Library adds image processing capabilities to your Python interpreter.
from PIL import Image
#  Keras Reduces cognitive load: it offers consistent & simple APIs
#  minimizes the number of user actions required for common use cases
#  clear & actionable error messages.
from keras.models import model_from_json
#serum is a fresh take on Dependency Injection in Python 3.
from serum import dependency, inject


# resize and preprocess image
# load machine learning model
# save model pickle
# input the image and predict
# return the results in form of json
# load json and create model

@dependency
@inject
class FileService:
    def __init(self):
        pass
    def prediction_results(self, filename):
        # resize and preprocess image
        # load machine learning model
        # save model pickle
        # input the image and predict
        # return the results in form of json
        # load json and create model
        labels = {1:'Bulging_Eyes', 2:'Crossed_Eyes', 3:'Glaucoma', 4:'Cataracts', 5:'Uveitis'}
        image = Image.open(f"files/{filename}")
        #resize image by given settings in the model
        image = tf.image.resize(image, (32, 32))
        #load model architecture from model.json
        with open('Service/model.json', 'r') as f:
            model_architecture = f.read()
        loaded_model = model_from_json(model_architecture)
        # load weights into the model architecture
        loaded_model.load_weights("Service/model.h5")
        # define loss func and optimizer
        # optimiser searchs for the minimun of the loss func when doing back propagation
        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        results = {}
        print(image[None].shape)
        #predict expects shape=(None, 32, 32, 3)
        prediction = loaded_model.predict(image[None])
        #return thee maximum probability value from 5 categories using argmax
        results['disease'] = labels[prediction.argmax(axis=1)[0]]
        return results