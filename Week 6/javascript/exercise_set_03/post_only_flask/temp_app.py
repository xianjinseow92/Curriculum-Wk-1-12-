from flask import Flask, request, jsonify
from flask_cors import CORS  # pip install flask-cors

from temp_api import convert_temp_from_unit

app = Flask(__name__)

# This line allows us to call the API from outside the Flask app
# CORS = Cross-Origin Resource Sharing
CORS(app)

@app.route('/convert_temperature', methods=['POST'])
def convert_temps():
    "Only route defined for this Flask app!"
    print(f"Input is {request.json}")

    try:
        result = convert_temp_from_unit(request.json['temperature'], request.json['unit'])
        status = 200
    except KeyError:
        result = {
            'message': 'Need to have input keys temperature and unit. Unit must be K, F, or C',
            'input': request.json
        }
        status = 400

    return jsonify(result), status

if __name__ == '__main__':
    app.run(debug=True)
