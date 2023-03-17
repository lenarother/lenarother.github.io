"""
Sign and verify JWT using Asymmetric Algorithm RSA.

https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/
"""

import datetime
import jwt
from secrets import PRIVATE_KEY_EC, PUBLIC_KEY_EC


# --- ENCODE ---
payload = {
    'sender': 'Magda',
    'message': 'JWT is awesome. You should try it!',
    'date': str(datetime.datetime.now()),
}
encoded_data = jwt.encode(
    payload=payload,
    key=PRIVATE_KEY_EC,
    algorithm='ES256',
)

print(encoded_data)


# --- DECODE ---
try:
    decode_data = jwt.decode(
        jwt=encoded_data,
        key=PUBLIC_KEY_EC,
        algorithms='ES256',
    )
    print(decode_data)

except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})
