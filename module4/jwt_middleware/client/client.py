import asyncio
import jwt

from fastmcp import Client

SECRET_KEY = "my-secret-key"


def create_jwt():
    return jwt.encode(
        {
            "sub": "donis",
            "role": "admin"
        },
        SECRET_KEY,
        algorithm="HS256"
    )


async def main():
    token = create_jwt()

    client = Client(
        "http://127.0.0.1:8000/mcp",
        auth=token,
    )

    async with client:
        result = await client.call_tool("admin_only_message", {})
        print(result)


asyncio.run(main())