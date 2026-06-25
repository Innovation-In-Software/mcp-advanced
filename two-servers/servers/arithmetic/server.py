from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "Arithmetic Tools",
    instructions="Provides arithmetic tools for addition, subtraction, multiplication, and division.",
)


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()