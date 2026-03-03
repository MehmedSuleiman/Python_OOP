from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 100
    PRICES = 5
    def __init__(self, name):
        super().__init__(name, self.PRICES, self.GRAMS, self.CALORIES)