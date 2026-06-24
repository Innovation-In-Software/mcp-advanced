# pip install pyjwt

import jwt
import os

secret = "my-secret-key"

token = jwt.encode(
    {
        "sub": "dmarshall",
        "role": "admin"
    },
    secret,
    algorithm="HS256"
)

print(token)