class TMDBPlugin(BasePlugin):
    name = "tmdb"
    description = "Provides movie and television metadata, including cast and crew."

    def search(self, query):
        # Implementation logic...
        return [UnifiedResult(canonical_id="TMDB456", title="Inception", entity_type="movie")]
