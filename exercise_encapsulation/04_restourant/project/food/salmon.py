from project.food.main_dish import MainDish


class Salmon(MainDish):
    CRAMS = 22

    def __init__(self, name, price, grams):
        super().__init__(name, price, self.CRAMS)