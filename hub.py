```python
class FederatedHub:
    def __init__(self):
        self.registry = {}

    def register_plugin(self, plugin):
        self.registry[plugin.name] = plugin

    def get_all_tool_definitions(self):
        return [p.get_tool_definition() for p in self.registry.values()]

    def run_search(self, query, active_sources):
        results = []
        for name in active_sources:
            if name in self.registry:
                results.extend(self.registry[name].search(query))
        return {r.canonical_id: r for r in results}.values()

```
