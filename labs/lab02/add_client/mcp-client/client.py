# execute client: python mcp-client/client.py
import asyncio
from fastmcp import Client

async def main():
    async with Client("../math/src/server.py") as client:
        result = await client.call_tool("add", {"a": 20, "b": 25})
        print(result)

asyncio.run(main())
