def recommend_from_cart(
        products,
        cart_items):

    recommendations = []

    cart_categories = []

    for pid in cart_items:

        if pid in products:

            cart_categories.append(
                products[pid]["category"]
            )

    for product in products.values():

        if product["category"] in cart_categories:

            recommendations.append(product)

    recommendations.sort(
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return recommendations[:5]