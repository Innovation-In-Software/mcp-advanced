import logging
from fastmcp import FastMCP, Context

# Step 1 — configure logging once at the top
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="audit.log"
)

# Step 2 — create a named logger for this module
logger = logging.getLogger(__name__)

mcp = FastMCP("Customer Server")

# Step 3 — write log messages inside your tools
@mcp.tool()
async def get_customer(customer_id: str, ctx: Context) -> str:
    """Look up a customer by ID"""

    # Server-side log — writes to audit.log on disk
    logger.info(f"TOOL_START | get_customer | customer_id={customer_id}")

    # Client-side log — sends message to the MCP client in real time
    await ctx.info(f"Looking up customer: {customer_id}")

    try:
        result = f"Customer {customer_id} data here"

        logger.info(f"TOOL_SUCCESS | get_customer | customer_id={customer_id}")
        await ctx.info("Lookup complete.")
        return result

    except Exception as e:
        logger.error(f"TOOL_ERROR | get_customer | customer_id={customer_id} | error={e}")
        await ctx.error(f"Something went wrong: {e}")
        raise

if __name__ == "__main__":
    mcp.run()