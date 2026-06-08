import heapq


def personalized_recommendation(
        products,
        search_history,
        cart_items,
        purchase_items):

    heap = []

    for product_id, product in products.items():

        score = 0

        if product["category"] in search_history:
            score += 2

        for item in cart_items:

            if item in products:

                if products[item]["category"] == product["category"]:
                    score += 3

        for item in purchase_items:

            if item in products:

                if products[item]["category"] == product["category"]:
                    score += 5

        heapq.heappush(
            heap,
            (-score, product_id)
        )

    recommendations = []

    visited = set()

    while heap and len(recommendations) < 5:

        score, pid = heapq.heappop(heap)

        if pid not in visited:

            visited.add(pid)

            recommendations.append(
                (pid, -score)
            )

    return recommendations