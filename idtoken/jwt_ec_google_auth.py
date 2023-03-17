"""
Sign and verify JWT using google-auth.

https://google-auth.readthedocs.io/en/master/index.html
"""

import datetime
import time

from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
from secrets import PRIVATE_KEY_EC


# --- ENCODE ---
payload = {
    "iss": "Magda",  # issuer of IDToken
    "azp": "Magda",  # authorized party (indicate the party that the IDToken was issued for)
    "aud": "Magda",  # audience intended audience or recipient for which the IDToken was issued
    "email": "rother.magdalena@gmail.com",
    "email_verified": "true",
    "iat": int(time.time()),  # issued at
    "exp": int((datetime.datetime.now() + datetime.timedelta(days=14000)).timestamp())  # expiration time
}


encoded_data = jwt.encode(
    payload=payload,
    key=PRIVATE_KEY_EC,
    algorithm='ES256',
)

print(encoded_data)


# --- DECODE ---
PUBLIC_KEY_URL = 'https://lenarother.github.io/keys/pub-ec.json'
AUDIENCE = 'Magda'
request = requests.Request()
claims = id_token.verify_token(
    encoded_data,
    request,
    AUDIENCE,
    PUBLIC_KEY_URL,
)

print(claims)
