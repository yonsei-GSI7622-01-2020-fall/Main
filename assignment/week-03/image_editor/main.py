from flask import Flask
from flask import request
from flask import render_template,url_for
from PIL import Image
import io
import base64
import cv2 
import numpy as np
app = Flask(__name__)


def resize_image(image):
    image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Converting BGR to RGB
    return image
    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resize', methods=['POST'])
def resize():
    file = request.files['file']
    image = np.array(Image.open(io.BytesIO(file.read()))) 
    
    image = resize_image(image)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, frame_encoded = cv2.imencode('.jpg', image, encode_param)
    prefix = 'data:image/jpeg;base64,'
    frame_base64 = prefix + base64.b64encode(frame_encoded).decode('utf-8')

    return frame_base64

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
