from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "Geometry and Series Tools",
    instructions="Provides slope, radius, and summation tools.",
)


@mcp.tool()
def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate the slope between two points."""
    if x1 == x2:
        raise ValueError("Slope is undefined for a vertical line.")
    return (y2 - y1) / (x2 - x1)


@mcp.tool()
def radius(diameter: float) -> float:
    """Calculate a circle radius from its diameter."""
    if diameter < 0:
        raise ValueError("Diameter must be non-negative.")
    return diameter / 2


@mcp.tool()
def summation(numbers: list[float]) -> float:
    """Return the sum of a list of numbers."""
    return sum(numbers)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()