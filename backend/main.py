from crypt import methods
from distutils.log import debug
from flask import Flask, request, render_template
from datetime import datetime
    
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/feed', methods=['POST'])
def feed():
    data_in = request.form
    # TODO: Do database stuff here
    
    return 'Ok'

@app.route('/', methods=['POST', 'GET'])
def index():
    data = []

    if request.method == 'POST':
        filters = {key: val for key, val in request.form.to_dict().items() if val}
        return_data = []
        for x in data:
            for key, val in filters.items():
                if val in data[key]:
                    return_data.append(x)
                    break
                
    else:
        return_data = data

    return render_template('index.html', data=return_data)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)