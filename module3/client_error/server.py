from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Client Error Demo")


@mcp.tool()
def divide_numbers(numerator: float, denominator: float) -> float:
	"""Divide two numbers and raise a clear client-facing error for invalid input."""
	if denominator == 0:
		raise ValueError("denominator must not be 0")
	return numerator / denominator


if __name__ == "__main__":
	mcp.run()
