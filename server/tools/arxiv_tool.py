import arxiv

def register(mcp):

    @mcp.tool()
    def search_arxiv(query: str) -> str:
        """Search research papers from Arxiv"""
        results = arxiv.Search(query=query, max_results=3).results()
        return "\n".join(
            f"{r.title} - {r.summary[:200]}" for r in results
        )
