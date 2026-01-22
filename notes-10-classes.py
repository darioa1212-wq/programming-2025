# Classes and Objects
# Author: Dario
# 11 December 2025

import random

class Pokemon:
    def __init__(self):
        """Constructor"""
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        print("A pokemon is born!")
        # 1 in 4096
        if random.randint(0, 4096):
            self.is_shiny = False
        else:
            self.is_shiny = True
            print("This pokemon is shiny!✨✨✨")

    def talk(self):
        """Hear what the pokemon has to say
        The pokemon says its species name"""
        print(f"{self.name} says, \"{self.species}\".")

    def stats(self):
        """Display the stats of the pokemon"""
        print(f"----({self.species})-----------")
        print(f"    Name:  {self.name}")
        print(f"    Type:  {self.type}")
        print(f"    Age:   {self.age}")
        print(f"    Level: {self.level}")
        print("--------------------------------")

    def find_something(self, how_many_things=1) -> list[str]:
        """Send pokemon to find something

        Returns:
            a list of str representing what it found"""
        things = ["pinap berry", "razz berry", "nanab berry", "golden razz berry", "leftovers", "moon stone"]
        found_things = []

        for _ in range(how_many_things):
            found_things.append(random.choice(things))

        return found_things

class Squirtle(Pokemon):
    def __init__(self):
        # Call the constructor of Pokemon
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"
        self.has_sunglasses = True

    def water_gun(self):
        """Squirtle shoots water out of its mouth"""
        print(f"{self.name} used water gun!")

class Mew(Pokemon):
    def __init__(self):
        # call the constructor of the parent class
        super().__init__()
        self.name = "Mew"
        self.type = "Psychic"
        self.species = "Mew"
        self.level = 1
        self.age = 0


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()

    # Access the pokemon's properties
    print("Pokemon name: ", pokemon_one.name)
    # Change the pokemone's properties
    pokemon_one.name = "Gary"
    pokemon_one.species = "Pikachu"
    print("Pokemon name: ", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    pokemon_two.species = "Pikachu"
    # Check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They're the same.")
    else:
        print("They're individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")

    # print(f"{pokemon_one.name} found these things: {pokemon_one.find_something()}")

    # Tell our pokemon to talk
    pokemon_one.talk()
    pokemon_two.talk()
    # Display stats of pokemon_one
    pokemon_one.stats()
    pokemon_two.stats()

    squirtle_one = Squirtle()
    # use .water_gun()
    squirtle_one.water_gun()
    # use .talk()
    squirtle_one.talk()

    # Create a Mew object
    pokemon_three = Mew()
    pokemon_three.talk()
    pokemon_three.stats()
