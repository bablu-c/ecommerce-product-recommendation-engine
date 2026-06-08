def get_top_products(products):

    all_products = list(
        products.values()
    )

    all_products.sort(
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return all_products[:10]