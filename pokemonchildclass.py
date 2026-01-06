# Pokemon Child Class
# Dario Androsevic
# December 17 2025


import random

class Pokemon:
    def __init__(self):
        """Constructor for the base Pokemon"""
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        print("A Pokemon is born!")


        if random.randint(1, 4096) == 1:
            self.is_shiny = True
            print("This Pokemon is shiny! ✨✨✨")
        else:
            self.is_shiny = False

    def talk(self):
        """Hear what the Pokemon says"""
        print(f"{self.name} says, \"{self.species}\".")

    def stats(self):
        """Display the stats of the Pokemon"""
        print(f"----({self.species})-----------")
        print(f"    Name:  {self.name}")
        print(f"    Type:  {self.type}")
        print(f"    Age:   {self.age}")
        print(f"    Level: {self.level}")
        print(f"    Shiny: {self.is_shiny}")
        print("--------------------------------")

    def find_something(self, how_many_things=1):
        """Pokemon searches for items"""
        things = ["pinap berry", "razz berry", "nanab berry", "golden razz berry", "leftovers", "moon stone"]
        found_things = [random.choice(things) for _ in range(how_many_things)]
        return found_things

    def dance(self, style="silly"):
        """Pokemon dances"""
        moves = ["wiggle", "spin", "jump"]
        move = random.choice(moves)
        print(f"{self.name} does a {style} dance: {move}! 💃🕺")


class Charmander(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Charmander"
        self.species = "Charmander"
        self.type = "fire"
        self.has_flame_tail = True

    def ember_attack(self):
        """Charmander uses Ember attack"""
        print(f"{self.name} used Ember! ")

    def warm_up(self):
        """Charmander warms itself up"""
        print(f"{self.name} is warming up by its tail flame! ")


    def dance(self, style="fiery"):
        moves = ["flame twirl", "spark jump", "tail spin"]
        move = random.choice(moves)
        print(f"{self.name} does a {style} dance: {move}!")


if __name__ == "__main__":
    char = Charmander()
    char.stats()
    char.talk()
    char.ember_attack()
    char.warm_up()
    char.dance()
    print(f"{char.name} found these items: {char.find_something(3)}")
