from flask import Flask
from flask import request,send_from_directory
from flask import render_template,url_for
from flask import Response, session, redirect
import json
from datetime import datetime
import time
import mysql.connector
import pandas as pd
import numpy as np
from datetime import timedelta

app = Flask(__name__, static_url_path='/static', 
            static_folder='static')

app.secret_key = b'mysecretkey'


app.permanent_session_lifetime = timedelta(minutes=5)


HOST = ""
USER = ""
PASSWORD = ""
mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  password=PASSWORD,
  database="yonflix"
)

@app.route('/')
def index():
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM movie ORDER BY RAND() LIMIT 10"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    for index, movie in enumerate(movies):
        movies[index]['image'] = movie['image'].split("?")[0]
    
    mycursor.close()

    return render_template("index.html", movies=movies)



@app.route('/register', methods=['POST'])
def register():
    username = request.values.get('username')
    
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM user WHERE username LIKE %s"
    val = (username,)
    

    
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    result = True
    if myresult:
        print(myresult)
        result = False
    else:
        session['username'] = username
        session.permanent = True
        sql = "INSERT INTO user (username) VALUES (%s)"
        val = (username,)
        
        mycursor.execute(sql, val)
        mydb.commit()
        session['user_id'] = mycursor.lastrowid
    mycursor.close()
    return Response(json.dumps({"result":result}),  mimetype='application/json')

@app.route('/signout', methods=['GET'])
def signout():
    
    session.clear()
    return redirect("/")

@app.route('/like_movie', methods=['POST'])
def like_movie():
    result = ""
    mycursor = mydb.cursor(dictionary=True)

    user_id = session['user_id']
    movie_id = request.values.get('movie_id')

    sql = "INSERT INTO `like` (user_id, movie_id) VALUES (%s,%s);"
    val = (user_id, movie_id)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    return Response(json.dumps({"result":result}),  mimetype='application/json')


@app.route('/user_based', methods=['GET'])
def user_based():
    
    result = []
    return Response(json.dumps({"result":result}),  mimetype='application/json')

@app.route('/content_based', methods=['POST'])
def content_based():
    time.sleep(1)
    username = session['username']
    
    mycursor = mydb.cursor(dictionary=True)
    
    sql = "SELECT * FROM user WHERE username LIKE %s"
    
    val = (username,)
    
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    
    user_id = myresult[0]['id']
    sql = "SELECT * FROM `like` INNER JOIN `movie` ON `like`.`movie_id` = `movie`.`id` WHERE `user_id` =  %s"
    val = (user_id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    
    recommended_movies = []
    for movie in myresult:
        movie_id = get_recommendations(movie['title'])
        if movie_id:
            recommended_movies.append(str(movie_id))
    result = []
    val = ",".join(recommended_movies)
    sql = "SELECT * FROM movie WHERE id IN ({})".format(val)
    
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mycursor.close()

    return Response(json.dumps({"result":result}),  mimetype='application/json')

def get_recommendations(title):
    with open('sim.npy', 'rb') as f:
        cosine_sim = np.load(f)

    indices = pd.read_csv("index.csv", header = None, index_col = 0, squeeze = True)
    try:
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:2]
        movie_indices = [i[0] for i in sim_scores]
        return movie_indices[0]+1
    except:
        return None

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
