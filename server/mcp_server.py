import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from mcp.server.fastmcp import FastMCP
from server.tools import arxiv_tool, math_tool, wiki_tool

mcp = FastMCP()

arxiv_tool.register(mcp)
math_tool.register(mcp)
wiki_tool.register(mcp)

if __name__ == "__main__":
    mcp.run()
