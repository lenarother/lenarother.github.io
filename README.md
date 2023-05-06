# JWT signing playground
![github metrics](github-metrics.svg)

[JSON Web Token (JWT)](https://jwt.io) is an open standard ([RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) 
for securely transmitting information between parties as a JSON object. 
This information can be verified and trusted because it is digitally signed. 
JWTs can be signed using a secret (with the HMAC algorithm) 
or a public/private key pair using RSA or ECDSA.
[Source](https://jwt.io/introduction).

Install requirements to try out examples in this repository.
```bash
pip install -r resources/requirements.txt
```

### Use a shared secret

[HS256 (HMAC with SHA-256)](https://en.wikipedia.org/wiki/HMAC) is a symmetric algorithm, with only one (secret) key 
that is shared between the two parties. The same key is used to generate the signature and to validate it.
To try it out you can create a random (secret) string and use jwt library to encode and decode it.
Code snippet.

```bash
python idtoken/jwt_hs256.py
```

### Use asymmetric public-private RSA keys

[RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is used to create public-private asymmetric key pair.
The token is signed using the private key of the RSA key pair.
The signature can be validated using freely accessible public key.


```bash
# generate jwtRS256.key and jwtRS256.key.pub
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key

# save public key in pam format
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub.2
```

Add 


Example of signing and verifying JWT (Json Web Token) using different algorithms.
- HMAC (symetric)
- RSA
- ECDSA

Example how to verify token using google auth and public key url
- https://lenarother.github.io/keys/pub-ec.json
- https://lenarother.github.io/keys/certs.json

Read more 
https://jwt.io/introduction

Generate RSA keys:

openssl ecparam -name prime256v1 -genkey -noout -out private.ec.key
openssl ec -in private.ec.key -pubout -out public.ec.pem

ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub.2
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub.2
openssl req -new -key jwtRS256.key -out jwtRS256.key.csr
openssl req -new -key jwtRS256.key -out jwtRS256.key.csr

