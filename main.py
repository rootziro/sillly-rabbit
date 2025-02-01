import hashlib
import secrets
import random
import string

# Generate a secure random password length of 20

password_length = 20
characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
password = ''.join(secrets.choice(characters) for i in range(password_length))

print("Password Generated", password)