class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, Storage):
        self.RAM = RAM
        self.Storage = Storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type is: {cls.storage_type}")

    # instance method
    def get_info(self):  # so this is instance method and we can call class atribute from this instance method. And it has 1st parameter as self.
        print(f"Laptop 1 has {self.RAM} RAM & {self.Storage} {self.storage_type}")


    @staticmethod
    def cal_discounted_price(price, discount):
        discount = (price - (price*discount/100))
        print(f"Discounted proce is: {discount}")
    


l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
# l1.get_info
# Laptop.get_storage_type()
Laptop.cal_discounted_price(40000,10)

