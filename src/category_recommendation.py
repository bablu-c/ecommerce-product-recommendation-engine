def category_recommendation(
        products,
        category):

    output = []

    for product in products.values():

        if product["category"].lower() == category.lower():

            output.append(product)

    output.sort(
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return output[:5]