# server.py
# Custom MCP server that exposes limited GitHub account/repo tools.
# The GitHub access token is supplied by OAuth2 and stored in an environment variable.

import os
import requests
from fastmcp import FastMCP

mcp = FastMCP("custom-github-oauth-server")

GITHUB_TOKEN = os.environ["GITHUB_OAUTH_TOKEN"]

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


@mcp.tool()
def github_me() -> dict:
    """
    Returns the GitHub account connected to this OAuth token.
    Useful for confirming the token belongs to the expected user.
    """
    response = requests.get(
        "https://api.github.com/user",
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def list_my_repos() -> list:
    """
    Lists repositories visible to this OAuth-authenticated GitHub account.
    Access depends on the OAuth scopes granted, such as repo or read:user.
    """
    response = requests.get(
        "https://api.github.com/user/repos",
        headers=HEADERS,
        params={"per_page": 20, "sort": "updated"},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # stdio is common for local MCP servers launched by VS Code, Claude Desktop, etc.
    mcp.run(transport="stdio")