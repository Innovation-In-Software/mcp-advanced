# pip install pyjwt

import jwt
import os

secret = "my-secret-key"

token = jwt.encode(
    {
        "user": "dmarshall",
        "role": "admin"
    },
    secret,
    algorithm="HS256"
)

print(token)