from project.animal import Animal


class Lion(Animal):
    def __init__(self,name:str, age:int, gender:str ):
        super().__init__(name, age, gender, money_for_care= 50)