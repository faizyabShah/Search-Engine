from flask import Flask, send_from_directory, jsonify, request
from queryParser import *

app = Flask(__name__, static_folder="client")


qp = queryParser()
