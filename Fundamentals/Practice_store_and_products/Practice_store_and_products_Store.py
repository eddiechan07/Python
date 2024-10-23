from Practice_store_and_products_Product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []              # Initialize an empty list to store products
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    # def sell_product(self, id):
    #     if 0<=id<len(self.products):
    #         sold_product = self.products.pop[id]
    #         print(f"Sold: {sold_product}")
    #     else:
    #         print("Invalid Product ID")
    #     return self
    def sell_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print(f"Sold: {product.name}")
                # return self
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self
    
    def print_info(self):
        for product in self.products:
            product.print_info()
        return self




