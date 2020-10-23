from flask import Flask
from flask import request,send_from_directory
from flask import render_template,url_for
from flask import Response
import json
from datetime import datetime
import time

app = Flask(__name__, static_url_path='/static', 
            static_folder='static')

def get_data(keyword):
    #TODO
    res = []
    for _ in range(10):
        page = {
            "link":"https://codethief.io",
            "title":keyword,
            "content":"오늘 하루도 고생 많으셨습니다",
        }
        res.append(page)
    return res


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    keyword = request.values.get('data')
    res = get_data(keyword)
    
    return Response(json.dumps(res),  mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
