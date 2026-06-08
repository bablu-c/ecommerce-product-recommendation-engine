def recommend_from_search_history(
        products,
        search_history):

    recommendations = []

    for product in products.values():

        if product["category"] in search_history:

            recommendations.append(product)

    recommendations.sort(
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return recommendations[:5]