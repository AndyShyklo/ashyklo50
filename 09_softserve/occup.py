'''
  Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K09 - Occupations and CSV
  2024-9-23
  time spent: 1.3 hours
'''

from flask import Flask
import random
import csv
app = Flask(__name__)           #create instance of class Flask

total = 0
d = {}
str1 = ""

@app.route("/")                 #assign fxn to route
def hello_world():
    global total, d, str1
    sum_v = 0
    r = random.uniform(0,total)
    for i in d:
        sum_v += d.get(i)
        if sum_v > r:
            return f"<h1>{i}: {d.get(i)}</h1> \n\n\n {str1}"
    return "none found"

def job_d():
    global total, d, str1
    with open("./occupations.csv", mode ='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if not lines.get('Job Class') == 'Total':
                d[lines.get('Job Class')] = float(lines.get('Percentage'))
                str1 = str1 + "\n" + lines.get('Job Class') + " | " + lines.get('Percentage') + "<br>"
            else:
                total = float(lines.get('Percentage'))
                
if __name__ == "__main__":      # true if this file NOT imported
    job_d()
    app.debug = True            # enable auto-reload upon code change
    app.run()
