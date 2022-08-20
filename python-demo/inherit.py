"""
Inheritance 

    Using the attributes and methods from one class in another class
     
    class Person():
        def __init__(self, attribute, attribute2):
    
    class Enemy(Person):
        def __init__(self, new_attribute, attribute, attribute2):
             super().__init__(self, attribute, attribute2)
             self.new_attribute = new attribute
"""

from OOP import Person

Maria = Person("Maria", "Adam", 95, status=True)
Rey = Person("Rey", "John", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=False)


class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.first_name))

    def steal(self, other):
        print("ha ha ha, {}, I have you stuff!".format(other.first_name))
        if other.status:
            other.status = False


Alex = Enemy("rock", "Alex", "Wayne", 75, status=False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)

"""
    multiple inheritance
        When one class inherits from multiple classes, and is able to use attributes and methods from both classes

        class Animal():
            def __init__(self, sound, look):
            ....

        class Place():
            def __init__(self, climate, lat, lon):
            ....
"""


# Parent class 1
class Item:
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))


# Parent class 2
class Garment:
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}".format(self.section, self.type))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale! ".format(self.color, self.name))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()

