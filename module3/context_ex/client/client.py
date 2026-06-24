import asyncio
from pathlib import Path

from fastmcp import Client
from fastmcp.client.logging import LogMessage


# Build the full path to the server file.
# This lets the client start the MCP server script from the parent folder.
SERVER_PATH = Path(__file__).resolve().parent.parent / "server.py"


async def show_server_log(message: LogMessage) -> None:
	# The server can send info messages while the tool is running.
	# This prints those messages in the client terminal.
	print(f"server {message.level.lower()}: {message.data}")


async def show_progress(progress: float, total: float | None, message: str | None) -> None:
	# Some tools report progress like 50 out of 100.
	# If the total exists, show both numbers.
	if total is not None:
		print(f"progress: {progress}/{total}")
	else:
		# If the server only sends one number, print that number by itself.
		print(f"progress: {progress}")

	# Some progress updates also include a text message.
	if message:
		print(f"progress message: {message}")


async def main() -> None:
	# Open a connection to the MCP server.
	# log_handler=show_server_log means server log messages will come here.
	async with Client(str(SERVER_PATH), log_handler=show_server_log) as client:
		# Call the greet tool on the server.
		# progress_handler=show_progress means progress updates are printed live.
		result = await client.call_tool(
			"greet",
			{"name": "Username"},
			progress_handler=show_progress,
		)
		# Print the final tool result after the server finishes its work.
		print(f"result: {result.data}")


if __name__ == "__main__":
	# Start the async program when this file is run directly.
	asyncio.run(main())
