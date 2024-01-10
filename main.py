from product import Product
from shopping_cart import ShoppingCart
from customer import Customer
from order import Order

# Create products
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Headphones", 50)

# Create a customer
customer = Customer("John Doe")

# Add products to the shopping cart
shopping_cart = ShoppingCart()
shopping_cart.add_product(product1, 2)
shopping_cart.add_product(product2, 1)
shopping_cart.add_product(product3, 3)

# Place an order
order_id = customer.place_order(shopping_cart)

# Display order details
customer.display_order(order_id)
