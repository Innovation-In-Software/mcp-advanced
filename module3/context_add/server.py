from fastmcp import Context, FastMCP


mcp = FastMCP("context-add")


@mcp.tool()
async def add(a: float, b: float, ctx: Context) -> float:
	"""Add two numbers and report the result to the client via context."""
	result = a + b
	await ctx.info(f"Computed result: {a} + {b} = {result}")
	return result


if __name__ == "__main__":
	mcp.run(transport="stdio")
