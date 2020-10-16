from flask import Flask
from flask import request
from flask import render_template,url_for
from PIL import Image
import io
import base64
import cv2 
import numpy as np
app = Flask(__name__)
import easyocr
reader = easyocr.Reader(['ko','en']) 


def get_ocr_info(image):
    #TODO
    info = "이 부분에 Easy OCR의 결과가 들어갑니다"
    return info
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['file']
    image = np.array(Image.open(io.BytesIO(file.read()))) 
    
    info = get_ocr_info(image)
    
    #TODO
    #이부분에 info에서 받은 정보를 기반으로 image에 박스를 그리는 작업을 진행합니다.
    
    
    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, frame_encoded = cv2.imencode('.jpg', image, encode_param)
    prefix = 'data:image/jpeg;base64,'
    frame_base64 = prefix + base64.b64encode(frame_encoded).decode('utf-8')
    return {"image":frame_base64,"ocr_info":" ".join(info)}

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
