# Two MCP Servers

This workspace contains two Python MCP servers:

- `servers/arithmetic/server.py` exposes `add`, `subtract`, `multiply`, and `divide`
- `servers/geometry/server.py` exposes `slope`, `radius`, and `summation`

## Setup

```powershell
uv sync
```

## Run Individually

```powershell
uv run servers/arithmetic/server.py
uv run servers/geometry/server.py
```

## VS Code MCP Configuration

Both servers are registered in `.vscode/mcp.json`, so a single workspace configuration exposes both MCP servers.