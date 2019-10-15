# -#- coding:utf-8 -#-
import random
class Petshop:
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet factory is our abstract factory.
        We can set it at well."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Cteates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("This is a lovely", str(pet))
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "dog"

class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"

class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"

class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"

def get_factory():
    """let's  be dynamoc!"""
    return random.choice([DogFactory, CatFactory])()
if __name__ == "__main__":
    shop = Petshop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)