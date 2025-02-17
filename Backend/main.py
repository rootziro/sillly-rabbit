import logging
import secrets
import string   
from Backend.storage import store_password
from Backend.scheduler import start_scheduler

# PLEASE NOTE: Add Error handling to the code below

# Logging config
logging.basicConfig(filename='app.log', level=logging.INFO)

# Generate a secure random password length of 20
password_length = 20
characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

# Secure random password
password = ''.join(secrets.choice(characters) for i in range(password_length))

secure_random_int = secrets.randbelow(100)

#Generate secure URL-safe token
secure_token = secrets.token_urlsafe(20)

store_password(password)

# non-sensitive logging
print("Password stored successfully")

start_scheduler()