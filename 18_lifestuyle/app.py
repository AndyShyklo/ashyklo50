'''Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K18 - Flask app with CSS
  2024-10-16
  time spent: 0.5 hours
'''

# DEMO
# basics of /static folder
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')    

if __name__ == "__main__":
    app.debug = True 
    app.run()