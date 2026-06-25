import mcp.types as mt
from fastmcp import Context, FastMCP
import logging
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "server.log"

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
    force=True,
)
logger = logging.getLogger("roots-demo-server")

mcp = FastMCP("Roots Demo Server")


async def handle_roots_list_changed(
    _: mt.RootsListChangedNotification,
) -> None:
    logger.info("Received notifications/roots/list_changed from client")


mcp._mcp_server.notification_handlers[mt.RootsListChangedNotification] = (
    handle_roots_list_changed
)


@mcp.tool()
async def show_roots(ctx: Context) -> str:
    """
    Server asks the client for its current roots.
    """
    roots = await ctx.list_roots()

    lines = []
    for root in roots:
        lines.append(f"{root.name}: {root.uri}")

    logger.info("Server requested roots:")
    for line in lines:
        logger.info("  %s", line)

    return "\n".join(lines) if lines else "No roots provided by client."


if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)