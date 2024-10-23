from Practice_store_and_products_Product import Product
from Practice_store_and_products_Store import Store


# Create a Store instance
store1 = Store("Seven-Eleven")

# Create some Product instances
product1 = Product("Strawberry", 5, "Fruit")
product2 = Product("Banana", 2, "Fruit")
product3 = Product("Grape", 3, "Fruit")
product4 = Product("Coco-cola", 2.5, "Drink")
product5 = Product("Sprite", 2.5, "Drink")

# Add products to the store
store1.add_product(product1).add_product(product2).add_product(product3).add_product(product4).add_product(product5)

# Print initial store inventory
store1.print_info()

# Sell product according to unique id, and re-print the store inventory
store1.sell_product(3).print_info()

# Apply inflation of 5% to all products, and print store inventory after inflation
print("After 5% inflation:")
store1.inflation(0.05).print_info()

# Apply a 20% clearance on all "Fruit" products, and print store inventory after applying clearance
print("After 2% clearance:")
store1.set_clearance("Fruit", 0.2).print_info()

