class Player:
    NO_GUILD = "Unaffiliated"

    def __init__(self, name:str, hp:int, mp:int) -> None:
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills :dict = {}
        self.guild = self.NO_GUILD

    def add_skill(self, skill_name: str, mana_cost:int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        result = [f"Name: {self.name}", f"Guild: {self.guild}",f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill_name, mana_cost in self.skills.items():
            result.append(f"==={skill_name} - {mana_cost}")

        return "\n".join(result)