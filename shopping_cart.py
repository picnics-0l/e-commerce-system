class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total
