from .base import BasePlugin, UnifiedResult
import requests

class OpenLibraryPlugin(BasePlugin):
    """
    Standard implementation for Open Library data fetching.
    """
    name = "open_library"
    description = "Searches for books, authors, and bibliographic data."

    def search(self, query: str) -> list[UnifiedResult]:
        url = f"https://openlibrary.org/search.json?q={query}"
        response = requests.get(url).json()
        
        unified_results = []
        for item in response.get('docs', []):
            unified_results.append(UnifiedResult(
                canonical_id=item.get('key', 'N/A'),
                title=item.get('title', 'Unknown'),
                entity_type='book',
                metadata={'authors': item.get('author_name', [])}
            ))
        return unified_results
