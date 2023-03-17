"""
Encode JWT with Symmetric Algorithm HS256 (HMAC with SHA-256).

https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/
"""

import datetime
import jwt

SECRET_KEY = 'python_jwt'

payload = {
    'sender': 'Magda',
    'message': 'JWT is awesome. You should try it!',
    'date': str(datetime.datetime.now()),
    # 'exp': datetime.datetime.utcnow() - datetime.timedelta(seconds=86400),  # Expired token
}
encode_data = jwt.encode(
    payload=payload,
    key=SECRET_KEY,
    algorithm='HS256',
)

print(encode_data)

try:

    decode_data = jwt.decode(
        jwt=encode_data,
        key=SECRET_KEY,
        algorithms="HS256"
    )
    print(decode_data)

except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})
