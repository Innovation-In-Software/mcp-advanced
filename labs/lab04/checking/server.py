import os
import jwt
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jwt-bank")

SECRET_KEY = os.environ.get("JWT_SECRET", "")
TOKEN = os.environ.get("JWT_TOKEN", "")


def validate_token():
    try:
        payload = jwt.decode(
            TOKEN,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload
    except Exception as ex:
        return None

############################
# Add withdraw tool here   #
############################



if __name__ == "__main__":
    mcp.run()