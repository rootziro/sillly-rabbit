# Create secure password storage Hashlib
import hashlib
import sqlite3
import os

def hash_password(password):
    #Random salt
    
    salt = os.urandom(20)

    # Hash password using PBKDF2 with 100,000 iterations and SHA-256
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Return salt and password hash
    return salt + password_hash

def store_password(password):
    password_hash = hash_password(password)

    # Connect to database and store password_hash
    conn = sqlite3.connect('secure_storage.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS passwords (password BLOB)')

    cursor.execute('INSERT INTO passwords (password) VALUES (?)', (password_hash,))
    conn.commit()
    conn.close()