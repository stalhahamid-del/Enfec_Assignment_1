import requests

class MCPClient:

    BASE_URL = "http://localhost:8001"

    @staticmethod
    def search(query: str):
        try:
            response = requests.get(
                f"{MCPClient.BASE_URL}/search",
                params={"query": query}
            )
            return response.json().get("result")
        except Exception as e:
            return f"MCP Error: {str(e)}"