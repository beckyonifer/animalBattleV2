# define character
class Character:

    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False

    def decrease_health(self, health_decrease) -> float:
        self.health -= health_decrease
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def display(self) -> None:
        print("Name: ", self.name, "\nStrength: ", self.strength, "\nHealth: ", self.health)

# define character types


class Cat(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
        self.characterType = "cat"

    def display(self) -> None:
        super().display()
        print("Type: ", self.characterType)


class Turkey(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
        self.characterType = "turkey"

    def display(self) -> None:
        super().display()
        print("Type: ", self.characterType)


class Spider(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
        self.characterType = "spider"

    def display(self) -> None:
        super().display()
        print("Type: ", self.characterType)
