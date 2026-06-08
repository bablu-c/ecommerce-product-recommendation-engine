import heapq

from similarity import calculate_similarity


class RecommendationEngine:

    def __init__(self, products):
        self.products = products

    def recommend(self, user_history, top_n=5):

        recommended = []

        purchased = set(user_history)

        for history_product in user_history:

            if history_product not in self.products:
                continue

            base_product = self.products[history_product]

            for product_id, product in self.products.items():

                if product_id in purchased:
                    continue

                score = calculate_similarity(
                    base_product,
                    product
                )

                heapq.heappush(
                    recommended,
                    (-score, product_id)
                )

        results = []

        visited = set()

        while recommended and len(results) < top_n:

            score, product_id = heapq.heappop(
                recommended
            )

            if product_id not in visited:

                visited.add(product_id)

                results.append(
                    (
                        product_id,
                        -score
                    )
                )

        return results