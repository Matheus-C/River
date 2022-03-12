from Animal import *


class Fish(Animal):
    # constructor
    def __init__(self, age = None, gender = None):
        if age == None:
            age = random.randint(0, 4)
        super().__init__(age, gender)
    # the class represented in string
    def __str__(self):
        fish = "F"
        fish += "F" if self.gender == Gender.FEMALE else "M"
        fish += str(self.getAge())
        return fish

    def maxAge(self):
        if self.getAge() >= 4:
            return True
        else:
            return False

    def getAge(self):
        return self.age

    def incrAge(self):
        alive = False
        if not self.maxAge():
            self.age += 1
            alive = True
        return alive

    def getGender(self):
        return self.gender