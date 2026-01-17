from client.llm import get_llm

from mcp.client.sse import sse_client
from mcp.client.session import ClientSession


async def run_agent(question: str):
    llm = get_llm()

    # Connect to MCP server via SSE
    async with sse_client("http://127.0.0.1:3333/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            tools = await session.list_tools()

            system_prompt = f"""
You are an intelligent Agentic AI.

Available MCP tools:
{tools}

Rules:
- Use Arxiv for research papers
- Use Wikipedia for explanations
- Use Math tools for calculations
"""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ]

            response = await llm.ainvoke(messages)
            return response.content
