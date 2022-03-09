from crypt import methods
from distutils.log import debug
from flask import Flask, request, render_template
    
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
def index():
    #                                                                         ||
                                                # Data should be of this form \/
    return render_template('index.html', data=[{'timestamp': 2020, 'proc_name': 'name', 'result': 'this is some text', 'link': 'google.com'}])

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)