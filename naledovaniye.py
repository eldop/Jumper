

class Animals():
    def __init__(self, age, name, weight):
        self.age = age
        self.name = name
        self.weight = weight

    def feed(self):
        self.weight += 0.5

    def hello(self):
        print('hello', self.name)


class Cat(Animals):
        def __init__(self, age, name, weight, color):
            Animals.__init__(self, age, name, weight)
            self.color = color

        def murchat(self):
            print('Мур')

girafe = Animals(5, 'Цыган', 12)
cat = Cat(2, 'чЕЧЕНЕц', 4, 'black')
girafe.hello()
cat.hello()
cat.murchat()
