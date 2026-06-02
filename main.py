```python
from fastapi import FastAPI
from hub import FederatedHub
from plugins import load_plugins

app = FastAPI()
hub = FederatedHub()

for plugin in load_plugins():
    hub.register_plugin(plugin)

@app.get("/tools")
def get_tools(): return hub.get_all_tool_definitions()

@app.post("/search")
def search(query: str, sources: list[str]): return hub.run_search(query, sources)

```
