class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        product = [p for p in self.products if p.name == product_name][0]
        return product

    def remove(self, product_name):
        product = [p for p in self.products if p.name == product_name]
        if product:
            self.products.remove(product[0])

    def __repr__(self):
        result = ""
        for i in range(len(self.products)):
            result += f"{self.products[i].name}: {self.products[i].quantity}"
            if not i == len(self.products) -1:
                result += "\n"
        return result
