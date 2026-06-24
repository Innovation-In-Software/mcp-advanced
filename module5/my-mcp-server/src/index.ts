import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" });

server.registerTool(
  "get_weather",
  {
    title: "Get Weather",
    description: "Fetches current weather for a city",
    inputSchema: { city: z.string() },
  },
  async ({ city }) => {
    return {
      content: [{ type: "text", text: `Weather for ${city}: sunny, 72°F` }],
    };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);