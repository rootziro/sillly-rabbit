import secrets
import string 
from storage import store_password

# Generate a secure random password length of 20
password_length = 20
characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

# Secure random password
password = ''.join(secrets.choice(characters) for i in range(password_length))

secure_random_int = secrets.randbelow(100)

#Generate secure URL-safe token
secure_token = secrets.token_urlsafe(20)

print("Password Generated", password)
print("Secure Random Integer", secure_random_int)
print("Secure Token", secure_token)

store_password(password)    