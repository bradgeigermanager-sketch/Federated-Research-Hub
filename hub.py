```python
class FederatedHub:
    def __init__(self):
        self.registry = {}

    def register_plugin(self, plugin):
        self.registry[plugin.name] = plugin
       
    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        """
        Returns a schema for all registered plugins.
        LLMs use this to 'see' what they can do.
        """
        tools = []
        for name, plugin in self.registry.items():
            tools.append({
                "type": "function",
                "function": {
                    "name": f"search_{name}",
                    "description": plugin.description,
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "The search term."}
                        },
                        "required": ["query"]
                    }
                }
            })
        return tools
        return [p.get_tool_definition() for p in self.registry.values()]

    def get_llm_tool_library(self) -> List[Dict]:
        """Generates the full list of tools for LLM tool-calling."""
        return [plugin.get_tool_definition() for plugin in self.registry.values()]
          
    def run_search(self, query: str, sources: list[str]):
        """
        The Hub acts as a router. The LLM tells us which 'sources' 
        it wants based on the tools it 'discovered'.
        """
        results = []
        for source_name in sources:
            if source_name in self.registry:
                # Execute the plugin search
                results.extend(self.registry[source_name].search(query))
        return {r.canonical_id: r for r in results}.values()
        return self.deduplicate(results)
        
import concurrent.futures

class SearchOrchestrator:
    def __init__(self, registry):
        self.registry = registry

    def federated_search(self, query: str, active_sources: list[str]):
        results = []
        # Parallel execution for speed
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_plugin = {
                executor.submit(self.registry[s].search, query): s 
                for s in active_sources if s in self.registry
            }
            
            for future in concurrent.futures.as_completed(future_to_plugin):
                try:
                    results.extend(future.result())
                except Exception as e:
                    print(f"Error in {future_to_plugin[future]}: {e}")
        
        return self._smart_merge(results)

    def _smart_merge(self, results):
        """Merges duplicate entities with priority logic."""
        merged = {}
        for r in results:
            if r.canonical_id not in merged:
                merged[r.canonical_id] = r
            else:
                # Priority: Newer metadata or from a more reliable plugin
                merged[r.canonical_id].metadata.update(r.metadata)
        return list(merged.values())
```
