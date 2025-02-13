from flask import Flask, request, jsonify
import secrets
import string
from storage import store_password

app = Flask(__name__) # Call function whenever a request is made to the root url.
app.route('/generate-password', methods=['POST'])