from flask import Flask, request, render_template

from db_feed import PostGreSQL

app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/feed', methods=['POST'])
def feed():
    data_in = request.form  # noqa:F841
    # TODO: Do database stuff here

    return 'Ok'


@app.route('/', methods=['POST', 'GET'])
def index():
    sql = PostGreSQL
    data = sql.fetch()

    if request.method == 'POST':
        print(request.form.to_dict())
        filters = request.form.to_dict()
        return_data = []
        for x in data:
            if filters['proc'] in data['proc'] and filters['result']:
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
