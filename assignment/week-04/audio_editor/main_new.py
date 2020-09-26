from flask import Flask
from flask import request,send_from_directory
from flask import render_template,url_for
from PIL import Image
import numpy as np
import scipy
import scipy.io.wavfile
import librosa
import soundfile as sf
from datetime import datetime
import time
app = Flask(__name__, static_url_path='/static', 
            static_folder='static')


def convert_audio(path):

    
    sample_rate, samples = scipy.io.wavfile.read(path)
    converted = samples.copy()
    #TODO

    
    
    sf.write(path, converted, sample_rate)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    dt = datetime.now()
    filename = str(int(time.mktime(dt.timetuple())))+".wav"
    path = "static/"+filename
    file.save(path)
    convert_audio(path)

    return path


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
