from fastmcp import FastMCP

mcp = FastMCP("math-mcp")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b


@mcp.resource("data://answer")
def answer() -> int:
    """Returns the answer to life, the universe, and everything."""
    return 42


if __name__ == "__main__":
    mcp.run(transport="stdio")
