 
from fastmcp import FastMCP
 
# Create the MCP server
mcp = FastMCP(name="code-review-server", version="1.0.0")
 
 
# Prompt: review-code
@mcp.prompt(
    "review_code",
    title="Code Review",
    description="Review code for best practices and potential issues",
)
def review_code(language: str, code: str) -> str:
    """
    Args:
        language: Programming language of the code
        code: The code to review
    """
    return f"Review this {language} code for best practices:\n\n{code}"
 
 
if __name__ == "__main__":
    mcp.run(transport="stdio")