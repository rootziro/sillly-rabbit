from flask import Flask, request, jsonify
import secrets
import string
from storage import store_password

app = Flask(__name__) # Call function whenever a request is made to the root url.
app.route('/generate-password', methods=['POST'])

def generate_password():
    password_length = 20
    characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password = ''.join(secrets.choice(characters) for i in range(password_length))
    secure_random_int = secrets.randbelow(100)
    secure_token = secrets.token_urlsafe(20)

    store_password(password)

    return jsonify({
        'password': password,
        'secure_random_int': secure_random_int,
        'secure_token': secure_token
    })

if __name__ == '__main__':
    app.run(debug=True)                                     