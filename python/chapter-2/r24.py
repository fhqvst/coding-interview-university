class Flower():

    def __init__(self, name='blossom', petals=5, price=20.50):
        self.__name = name
        self.__petals = petals
        self.__price = price


    @property
    def name(self):
        return self.__name

    @property
    def petals(self):
        return self.__petals

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        self.__name = name

    @petals.setter
    def petals(self, petals):
        self.__petals = petals

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('price cannot be less than 0')

        self.__price = price

if __name__ == '__main__':
    a = Flower()
    b = Flower('flowy', 4, 33)

    print(a.name)
    print(b.name)

    b.price = -1
