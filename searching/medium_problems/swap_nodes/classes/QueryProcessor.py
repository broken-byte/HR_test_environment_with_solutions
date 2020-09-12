

class QueryProcessor:

    def __init__(self, queries: list):
        self.queries: list = queries
        self.processed_queries: list = []

    def process_queries_with_depth_limit(self, depth_limit: int) -> list:
        for k in self.queries:
            depths_to_be_swapped: list = []
            multiple: int = 1
            product: int = multiple*k
            while product <= depth_limit:
                depths_to_be_swapped.append(product)
                multiple += 1
                product = multiple * k
            self.processed_queries.append(depths_to_be_swapped)
        return self.processed_queries.copy()
