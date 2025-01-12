import hmac
import hashlib
import secrets
import string

def generate_hmacpasswd(master_key, service_name, length=16, use_special_chars=True):

 # 1. Generate deterministic base using HMAC with sha-256
 base_hash = hmac.new(
  master_key.encode()
  service_name.encode()
  hashlib.sha256

 ).hexdigest()
# 2. Generate random chars using 'secrets' module
additional_chars = string.ascii_letters + string.digits
if use_special_chars: # type: ignore
 additional_chars+= string.punctuation