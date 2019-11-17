# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

from flask import Flask
from predictor_api import make_prediction, feature_names


app = Flask(__name__)  # create instance of Flask class


@app.route("/predict", methods=["POST", "GET"])  # the site to route to, index/main in this case
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name )as set in template" (key): "string in the textbox" (value)
    x_input, predictions = make_prediction(request.args) 
    return flask.render_template

if __name__ == '__main__':
    app.run()



