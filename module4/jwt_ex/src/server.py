# $env:JWT_SECRET="my-secret-key"
# $env:JWT_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# set JWT_SECRET=my-secret-key
# set JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

import os
import jwt
from mcp.server.fastmcp import FastMCP

# Read values from environment variables
SECRET_KEY = os.environ["JWT_SECRET"]
TOKEN = os.environ["JWT_TOKEN"]

mcp = FastMCP("jwt-demo-server")


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


@mcp.tool()
def delete_user(username: str) -> str:
    """Delete a user (requires admin role in JWT token)."""
    claims = validate_token()

    if not claims:
        return "Access Denied: Token invalid"

    if claims["role"] != "admin":
        return "Not Authorized: admin role required"

    return f"Deleted user: {username} (requested by {claims['user']})"


if __name__ == "__main__":
    mcp.run()