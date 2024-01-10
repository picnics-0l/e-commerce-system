class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = {}

    def place_order(self, shopping_cart):
        order_id = len(self.orders) + 1
        order = Order(order_id, shopping_cart)
        self.orders[order_id] = order
        return order_id

    def display_order(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            print(f"Order ID: {order.order_id}")
            print("Products:")
            for product, quantity in order.shopping_cart.products.items():
                print(f"{product.name}: {quantity}")
            print(f"Total: ${order.shopping_cart.calculate_total()}")
        else:
            print(f"Order with ID {order_id} not found.")
