"""
Sign and verify JWT using Asymmetric Algorithm RSA.

https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/
"""

import datetime
import jwt
from secrets import PRIVATE_KEY, PUBLIC_KEY


# --- ENCODE ---
payload = {
    'sender': 'Magda',
    'message': 'JWT is awesome. You should try it!',
    'date': str(datetime.datetime.now()),
    # 'exp': datetime.datetime.utcnow() - datetime.timedelta(seconds=86400),  # Expired token
}
encoded_data = jwt.encode(
    payload=payload,
    key=PRIVATE_KEY,
    algorithm='RS256',
)

print(encoded_data)


# --- READ WITHOUT VERIFICATION ---
print(jwt.decode(encoded_data, options={'verify_signature': False}))


# --- DECODE ---
try:
    decode_data = jwt.decode(
        jwt=encoded_data,
        key=PUBLIC_KEY,
        algorithms='RS256',
    )
    print(decode_data)

except Exception as e:
    message = f'Token is invalid --> {e}'
    print({'message': message})


