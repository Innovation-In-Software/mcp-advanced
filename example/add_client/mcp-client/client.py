# execute client: python mcp-client/client.py
import asyncio
from fastmcp import Client

async def main():
    async with Client("../math/src/server.py") as client:
        result = await client.call_tool("add", {"a": 20, "b": 25})
        print(result)
        result = await client.call_tool("subtract", {"a": 25, "b": 5})
        print(result)
        result = await client.call_tool("multiply", {"a": 10, "b": 12})
        print(result)
        result = await client.call_tool("divide", {"a": 18, "b": 3})
        print(result)

asyncio.run(main())
