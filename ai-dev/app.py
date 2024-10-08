from flask import Flask,render_template
import psycopg2
from config import login_config
from connect import connect

app = Flask(__name__)



@app.route("/")
def hello_world():
    config = login_config()
    conn = connect(config)
    
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            result = cursor.fetchall()
            print(result)

    return render_template("index.html")