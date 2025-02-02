# Create secure password storage Hashlib
import hashlib
import os

def hash_password(password):
    #Random salt

    salt = os.urandom(20)

    # Hash password using PBKDF2 with 100,000 iterations and SHA-256
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Return salt and password hash
    return salt + password_hash