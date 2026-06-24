from fastmcp import FastMCP, Context

mcp = FastMCP("Demo Server")

@mcp.tool()
async def greet(name: str, ctx: Context) -> str:
    """Greet a user by name"""

    await ctx.info(f"Starting greeting for: {name}")
    result = f"Hello, {name}!"
    await ctx.info("Done.")
    return result


if __name__ == "__main__":
    mcp.run()