from Animal import *


class Bear(Animal):
    # constructor
    def __init__(self, age = None, gender = None, strength = None):
        if strength == None:
            self.strength = random.randint(0, 5)
        if age == None:
            age = random.randint(0, 9)
        super().__init__(age, gender)
# the class represented in string
    def __str__(self):
        bear = "B"
        bear += "F" if self.gender == Gender.FEMALE else "M"
        bear += str(self.getAge())
        return bear

# Get the current strength of the bear.
    def getStrength(self):
        return self.strength

    def maxAge(self):
        if self.getAge() >= 9:
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