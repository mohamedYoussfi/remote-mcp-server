from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os

from typing import Dict, List

load_dotenv()

TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
search_client = TavilyClient(TAVILY_API_KEY)

mcp_server = FastMCP("web-search-mcp-server", port=21000, host="0.0.0.0")


@mcp_server.tool()
def employee_info(name: str) -> Dict:
    """
    Get information about the given employee
    """
    return {"name": name, "salaty": 6500, "job": "Developper"}


@mcp_server.tool()
def web_search(query: str) -> List[Dict]:
    """
    Use this tool to search the web for information
    Args:
      query : The search query
    Returns:
      The search Results
    """

    try:
        response = search_client.search(query=query)
        return response["results"]
    except:
        return "No results found"


if __name__ == "__main__":
    mcp_server.run(transport="sse")
