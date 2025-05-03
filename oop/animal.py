# oop/animal.py

class Animal:
    def __init__(self, name, color):
        self.name = name  # Instance attribute for the animal's name
        self.color = color  # Instance attribute for the animal's color

    def get_animal_name(self):
        print(f"The animal name is {self.name}")  # Print the animal's name

    def get_animal_color(self):
        print(f"The color of the animal is {self.color}")  # Print the animal's color
    def get_animal_info(self):
        print(f"Animal name is {self.name} and the color is {self.color}")
