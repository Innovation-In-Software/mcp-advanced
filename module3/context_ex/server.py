from fastmcp import FastMCP, Context
import asyncio

mcp = FastMCP("Context Demo")


@mcp.tool()
async def greet(name: str, ctx: Context) -> str:
    """
    Demonstrates using the Context object.
    """

    # Send a message to the MCP client
    await ctx.info(f"Starting greeting for {name}")

    # Simulate work
    await asyncio.sleep(2)

    # Send progress update
    await ctx.report_progress(50, 100)

    await asyncio.sleep(2)

    # Send another message
    await ctx.info("Almost finished")

    # Return final result
    return f"Hello {name}!"


if __name__ == "__main__":
    mcp.run()