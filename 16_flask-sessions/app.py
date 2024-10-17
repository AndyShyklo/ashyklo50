"""
Andy Shyklo, Ankita Saha, Abidur Rahman
Python Pigs
SoftDev
K16 - flask sessions
2024-10-9
time spent: 1.5 hr
"""

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
from flask import redirect

import textmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = b'_5#j812jwwjkKLWio)2u'


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("Logging in")
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    if 'username' in session:
        return redirect("/auth")
    return render_template( 'login.html' )

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("Authenticating")
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    if 'username' in session:
        return(render_template('response.html', username = session["username"], password = session["password"]))
    #print("***DIAG: request.args['username']  ***")
    #print(request.form.get['username'])
    #print("***DIAG: request.args['password']  ***")
    #print(request.form.get['password'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    if request.method == 'POST':
        session['username']=request.form.get('username')
        session['password']=request.form.get('password')
        return(render_template('response.html', username = session["username"], password = session["password"]))
    else:
        return "<h1>Error!</h1>"
    
@app.route("/logout", methods=['GET', 'POST'])
def disp_logoutpage():
    print("Logging out")
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    se = session["username"]
    session.clear()
    return render_template( 'logout.html', usr = se)
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
