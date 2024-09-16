class Fruit():
    def __init__(self, fruit):
        query = input("Enter the name of a  fruit")
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

print(dir(Fruit))