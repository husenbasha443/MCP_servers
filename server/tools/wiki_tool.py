import wikipedia

def register(mcp):

    @mcp.tool()
    def search_wikipedia(topic: str) -> str:
        """Get Wikipedia summary"""
        return wikipedia.summary(topic, sentences=3)
