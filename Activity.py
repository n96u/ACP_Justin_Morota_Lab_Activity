#class method
class Product:
    inventory = []
    product_counter = 0
    #__init__ constructor
    def __init__(self, name, category, quantity, price, supplier):
        Product.product_counter += 1
        self.product_id = Product.product_counter
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)
    #add product    
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls(name, category, quantity, price, supplier)
        return "Product added successfully"
    #update product
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"
    #delete product
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"
    #display product
    @classmethod
    def display_inventory(cls):
        if not cls.inventory:
            print("No products in inventory.")
        else:
            for product in cls.inventory:
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                      f"Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier}")
#another class
class Order:
    def __init__(self, order_id, product_id, quantity, customer_info=None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info

    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                return f"Order placed successfully. Order ID: {self.order_id}"
        return "Product not found. Order cannot be placed."

# Sample Flow
if __name__ == "__main__":
    print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
    print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
    print(Product.update_product(1, quantity=45, price=950))
    print(Product.delete_product(2))
    order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
    print(order1.place_order())
    print("\nCurrent Inventory:")
    Product.display_inventory()