class ProductStore:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        ProductStore.count+=1

    @classmethod
    def get_totalProducts(cls):
        print(f"Total products in a store is: {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        discount = price - (price*discount/100)
        print(f"Discount on the product is: {discount}")


p1 = ProductStore("TV", 50000)
p2 = ProductStore("Mobile", 80000)
P3 = ProductStore("Laptop", 75000)
ProductStore.get_totalProducts()
ProductStore.get_discount(p1.price, 12)



        