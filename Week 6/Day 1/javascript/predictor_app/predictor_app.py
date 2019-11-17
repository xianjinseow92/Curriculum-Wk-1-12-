import flask
from flask import request, jsonify
from predictor_api import make_api_prediction, feature_names

# Initialize the app

app = flask.Flask(__name__)

# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
@app.route("/")
def hello():
    return "It's alive!!!"

@app.route("/predict", methods=["GET"])
def get_predict_page():
    "Returns the rendered page"
    # We can try other template pages as well.
    # Change this line to any of the other html files in the template folder
    # Described in README
    return flask.render_template('predictor_javascript_simple.html')

@app.route("/predict_api", methods=["POST"])
def get_api_response():
    # This function will throw an error if we are missing one of
    # the features it expects. Any status code that is not 200 - 299
    # is flagged as an error
    try:
        response = make_api_prediction(request.json)
        status = 200
    except KeyError:
        missing = [f for f in feature_names if f not in request.json]
        response = {
            'status': 'error',
            'msg': f'not all required feature names ({feature_names}) present. Missing {missing}'
        }
        status = 300
    return jsonify(response), status


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
