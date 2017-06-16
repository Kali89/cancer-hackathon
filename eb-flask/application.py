from flask import Flask, jsonify
application = Flask(__name__)

@application.route('/')
def homepage_predictions():
    result = {'result': 0.1}
    return jsonify(result)

@application.route('/predictions')
def get_predictions():
    result = {'result': 0.5}
    return jsonify(result)

if __name__ == "__main__":
    application.debug = True
    application.run()
