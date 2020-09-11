from flask import Flask
from flask import request
from flask import render_template,url_for


app = Flask(__name__)


def get_text_analysis(text=""):
    
    if not text:
        return {}
    print(text)
    num_of_chars = len(text)
    num_of_words = len(text.split())
    num_of_lines = len(text.split("\n"))
    
    
    return {
        "num_of_chars":num_of_chars,
        "num_of_words":num_of_words,
        "num_of_lines":num_of_lines
        
    }
    
    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        text = request.values.get('data')
    else:
        text = request.args.get('text', "No text")
    if text:
        result = get_text_analysis(text)
    else :
        result = {}
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
