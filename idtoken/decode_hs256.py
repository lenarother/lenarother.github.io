"""
Decode JWT with Symmetric Algorithm HS256 (HMAC with SHA-256).

https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/
"""

import jwt

SECRET_KEY = "python_jwt"

valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZW5kZXIiOiJNYWdkYSIsIm1lc3NhZ2UiOiJKV1QgaXMgYXdlc29tZS4gWW91IHNob3VsZCB0cnkgaXQhIiwiZGF0ZSI6IjIwMjMtMDMtMTcgMTE6Mjg6MzQuNTg0Nzc0In0.pFSoPPg1bm1Qz46QlDqbNzzIDcAdJzKf2v9UQCZ_-nU"
# Expired token
# invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZW5kZXIiOiJNYWdkYSIsIm1lc3NhZ2UiOiJKV1QgaXMgYXdlc29tZS4gWW91IHNob3VsZCB0cnkgaXQhIiwiZGF0ZSI6IjIwMjMtMDMtMTcgMTE6MjY6MTMuNDU2MzI2IiwiZXhwIjoxNjc4OTYyMzczfQ.x8fIr3Ufy79-9e1ZUdYiJh6RLsH2jmHOCrC3pSdW_0I"

try:

    decode_data = jwt.decode(
        jwt=valid_token,
        key=SECRET_KEY,
        algorithms="HS256"
    )
    print(decode_data)

except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})
