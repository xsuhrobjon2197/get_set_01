#2-m
class Car:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new):
        self.__price = new
        
    
c1 = Car('BMW', 45000)
print(c1.name)

res = c1.price
print(res)

c1.price = 5000
print(c1.price)
