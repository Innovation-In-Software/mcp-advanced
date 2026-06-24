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


@mcp.tool()
def withdraw(amount: float) -> str:
    """Attempt a withdrawal. Checks JWT claims to enforce the max allowed amount."""
    claims = validate_token()
    if not claims:
        return "Access Denied: Token invalid or missing."

    name = claims.get("name", "Unknown")
    max_amount = claims.get("max", 0)

    if amount > max_amount:
        return (
            f"Error: Withdrawal of ${amount:.2f} exceeds the maximum "
            f"allowed amount of ${max_amount:.2f} for {name}."
        )

    return f"Success: ${amount:.2f} has been withdrawn for {name}."


if __name__ == "__main__":
    mcp.run()