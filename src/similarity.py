def calculate_similarity(product1, product2):

    score = 0

    # Same Category
    if product1["category"] == product2["category"]:
        score += 5

    # Same Brand
    if product1["brand"] == product2["brand"]:
        score += 3

    # Similar Price Range
    price1 = float(product1["price"])
    price2 = float(product2["price"])

    if abs(price1 - price2) <= 5000:
        score += 2

    # Product Rating Bonus
    score += float(product2["rating"])

    return score