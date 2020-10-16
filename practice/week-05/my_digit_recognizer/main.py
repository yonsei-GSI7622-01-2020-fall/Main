from flask import Flask
from flask import request
from flask import render_template,url_for
from PIL import Image

import io
import base64
import cv2 
import numpy as np
import urllib
from joblib import dump, load
from binascii import a2b_base64

import tensorflow as tf
model = tf.keras.models.load_model('my_model.h5')
clf = load('my_digit_model.joblib')
app = Flask(__name__)
def resize_image(image):
    image = cv2.resize(image, (28,28)) 
    return image
    
def recognize_image(image, is_tf = False):
    if is_tf:
        print("tensorflow")
        image = image/255.0
        
        return "TF",model.predict_classes( np.array( [image,] ))

    else:
        print("sklearn")
        image = image.reshape(1, -1)
        
        return "SK",clf.predict(image)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recognize', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        data_url = request.values.get('data')
        model_type = request.values.get('type')
        encoded_image = data_url.split(",")[1]
        binary_data = a2b_base64(encoded_image)

        
        data_io = io.BytesIO(binary_data)
        img = Image.open(data_io)
        

        image_np = np.array(img)
        
        image_np = image_np[:, :, 3]
        
        
        resized = resize_image(image_np)
        
        
        model_type = False if model_type == "0" else True
        a = recognize_image(resized, is_tf=model_type)
        

        

    return str(a)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
