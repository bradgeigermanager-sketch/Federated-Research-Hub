from fastapi import FastAPI
from hub import FederatedHub
from plugins import load_plugins

app = FastAPI()
hub = FederatedHub()

# Dynamically load and register all plugins found in plugins/
for plugin in load_plugins():
    hub.register_plugin(plugin)

@app.get("/tools")
def get_tools():
    """LLM Discovery: Returns all available tool definitions."""
    return hub.get_all_tool_definitions()

@app.post("/search")
def search(query: str, sources: List[str]):
    """LLM Execution: Returns deduplicated results."""
    return hub.run_search(query, sources)
