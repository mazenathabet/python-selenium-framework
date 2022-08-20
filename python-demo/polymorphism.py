"""
    Polymorphism
    ( method overriding)

    override a method from the parent class with the same exact name in the child class
"""

from OOP import Person

Maria = Person("Maria", "Adam", 95, status=True)
Rey = Person("Rey", "John", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=False)


class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

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

Maria.introduce()
" Introduce method from the person class (Parent)"
Rey.introduce()
" Introduce method from the person class (Parent)"
Alex.introduce()
" Introduce method from the Enemy class (child) "
