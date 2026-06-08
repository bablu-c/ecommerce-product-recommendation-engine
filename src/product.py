class Product:
    def __init__(self, product_id, name, category, brand, price, rating):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = brand
        self.price = float(price)
        self.rating = float(rating)

    def display(self):
        print(
            self.product_id,
            self.name,
            self.category,
            self.brand,
            self.price,
            self.rating
        )