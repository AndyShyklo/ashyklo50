"""
Andy Shyklo, Ankita Saha, Abidur Rahman
Python Pigs
SoftDev
K14 - intake and forms
2024-10-07
time spent: 1 hr
"""

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import textmod0
'''Why is it not textmod0.py instead of textmod0? We think that at the import of import testmod0.py, it will not print what is under the if statement
or the goo method in textmod0.py, but just print the plain print statements that aren't under any method/statement.'''

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


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
#We don't know what these methods do, but maybe they just take from the base request of the user.
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #This requests the arguments of the methods when accessing it, like the GET and POST methods, when given.
    #print("***DIAG: request.args['username']  ***")
    # Where does it get the username from? What is it requesting from? We think it could be from the original methods at the top.
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    return render_template( 'login.html' )
'''Here, We are unsure about what the methods and ***DIAG:*** means, but we think it might be some parameter that is
inputted when you access, either given from another method or your access info. We think the DIAG means is trying
to request information about login and such, step by step, in order to gain secure and accurate info.
Also, there will a request to load login.html with render_template, but it looks to be called somewhat in a weird way.'''

@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission
'''
When the /auth is requested, via the submission form, the page will just show "Waaaa hooo HAAAH", but we don't know what many of the DIAG and GET or POST things do in the code.
'''

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
