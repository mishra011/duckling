
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from duckling import DucklingWrapper

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

wrapper = DucklingWrapper()


@app.route('/parse',methods=['POST'])
def duckling_wrapper():
    data = request.form
    query = data['text'].lower()
    response = wrapper.parse(query)
    return  jsonify(response)

@app.route('/tester',methods=['POST'])
def test_ducking():
    data = request.json
    query = data['text']
    response = wrapper.parse(query)

    return  jsonify(response)


app.run(host='0.0.0.0',port=4000)

