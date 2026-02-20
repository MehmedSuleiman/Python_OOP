class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    def defend(self, points: int) -> str | None:
        self.health -= points
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
    def heal(self, points: int) -> int:
        self.health += points


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
