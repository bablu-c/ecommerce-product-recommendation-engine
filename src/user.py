class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        self.views = []
        self.cart = []
        self.purchases = []

    def add_view(self, product_id):
        self.views.append(product_id)

    def add_cart(self, product_id):
        self.cart.append(product_id)

    def add_purchase(self, product_id):
        self.purchases.append(product_id)