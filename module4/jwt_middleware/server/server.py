from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_context, get_http_headers
import jwt

SECRET_KEY = "my-secret-key"


def get_bearer_token() -> str | None:
    headers = get_http_headers(include_all=True)
    auth_header = headers.get("authorization") or headers.get("Authorization")
    if not auth_header:
        return None

    scheme, _, token = auth_header.partition(" ")
    if scheme.lower() != "bearer" or not token:
        return None
    return token


class RoleMiddleware(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        token = get_bearer_token()

        if token is None:
            raise PermissionError("Missing JWT token")

        # For a real app, verify issuer, audience, expiration, etc.
        claims = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        if context.fastmcp_context is None:
            raise PermissionError("Missing request context")

        context.fastmcp_context.set_state("user", {
            "id": claims.get("sub"),
            "role": claims.get("role")
        })

        return await call_next(context)


mcp = FastMCP(
    "secure-server",
    middleware=[RoleMiddleware()]
)


@mcp.tool()
async def admin_only_message() -> str:
    user = get_context().get_state("user")
    if not user:
        raise PermissionError("Missing user context")

    if user.get("role") != "admin":
        raise PermissionError("Access denied. Admin role required.")

    return f"Hello {user.get('id')}. You are an admin."


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
        path="/mcp"
    )