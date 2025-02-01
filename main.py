import hashlib
import secrets
import random
import string
import os

# Generate a secure random password length of 20
password_length = 20
characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

# Secure random password
password = ''.join(secrets.choice(characters) for i in range(password_length))

print("Password Generated", password)

# Create secure password storage Hashlib
def hash_password(password):
    #Random salt

    salt = os.urandom(20)

    # Hash password using PBKDF2 with 100,000 iterations and SHA-256
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)