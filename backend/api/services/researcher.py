from .mcp_client import MCPClient

class ResearchAgent:

    @staticmethod
    def execute(plan: str):
        if "Need to search for:" in plan:
            query = plan.replace("Need to search for:", "").strip()
            return MCPClient.search(query)
        return "No research executed."