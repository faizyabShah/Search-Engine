from flask import Flask, send_from_directory, jsonify, request
from queryParser import *

app = Flask(__name__, static_folder="client")


qp = queryParser()


@app.route('/')
def index():
    return send_from_directory("client", "index.html")


@app.route('/style.css')
def style():
    return send_from_directory("client", "style.css")


@app.route('/script.js')
def script():
    return send_from_directory("client", "script.js")


@app.route('/search', methods=['get'])
def search():
    params = request.args['q']
    params = params.split()
    print(params)
    data = qp.search(params)
    return data[:20]

    # Do something with the data


if __name__ == '__main__':
    app.run()
