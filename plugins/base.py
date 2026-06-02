```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, List

@dataclass
class UnifiedResult:
    canonical_id: str
    title: str
    entity_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class BasePlugin(ABC):
    name: str = "base"
    description: str = "Base plugin"

    @abstractmethod
    def search(self, query: str) -> List[UnifiedResult]:
        pass

    def get_tool_definition(self) -> Dict[str, Any]:
        return {
            "name": f"search_{self.name}",
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"]
            }
        }

```
