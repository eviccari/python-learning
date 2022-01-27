class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    # if we comment setter method, the property turns to "read only" access type
    @price.setter
    def price(self, price):
        if(price < 1):
            raise ValueError("Price cannot be less than 1")
        self.__price = price

try:
    product = Product(-10)
    print(product.price)

    product.price = 5
    print(product.price)
except ValueError as error: 
    print(error)
