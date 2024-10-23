class Product:
    unique_id = 1
    def __init__(self, name, price, category):
        self.id = Product.unique_id
        Product.unique_id +=1
        self.name = name
        self.price = price
        self.category = category
        
    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    
    def print_info(self):
        print (f"Product Name: {self.name}| Price: {self.price}| Category: {self.category}")
