import os
import jwt

SECRET_KEY = os.environ["JWT_SECRET"]
TOKEN = os.environ["JWT_TOKEN"]

print(SECRET_KEY)
print(TOKEN)