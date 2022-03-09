from crypt import methods
from distutils.log import debug
from flask import Flask, request
    
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/feed', methods=['POST'])
def feed():
    data_in = request.form
    # TODO: Do database stuff here
    
    return 'Ok'

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)