from mcp.server.fastmcp import FastMCP

# Create the server instance, specifying host and port
mcp = FastMCP(
    name="my-http-server",
    host="127.0.0.1",   # use 0.0.0.0 to accept connections from other machines
    port=8765,
)

# Define a simple tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

# Start the server using Streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")