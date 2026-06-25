import asyncio
from pathlib import Path

import mcp.types as mt
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import Root


class ChangingRoots:
    def __init__(self):
        self.roots = [
            Root(
                uri=Path("project_a").resolve().as_uri(),
                name="Project A",
            )
        ]

    async def list_roots(self, _context):
        return mt.ListRootsResult(roots=self.roots)

    def change_roots(self):
        self.roots = [
            Root(
                uri=Path("project_b").resolve().as_uri(),
                name="Project B",
            )
        ]


async def main():
    root_state = ChangingRoots()

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read,
            write,
            list_roots_callback=root_state.list_roots,
        ) as session:
            await session.initialize()

            print("Connected to server and finished MCP initialize.")

            print("\nInitial roots:")
            result = await session.call_tool("show_roots", {})
            print(result.content[0].text)

            print("\nChanging client roots...")
            root_state.change_roots()

            await session.send_roots_list_changed()

            print("\nRoots after change:")
            result = await session.call_tool("show_roots", {})
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())