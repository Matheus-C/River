from abc import ABC, abstractmethod, abstractproperty
import random
from enum import Enum
from xml.etree.ElementInclude import LimitedRecursiveIncludeError
##
# Enumerated type representing possible genders
# of animal s i n the Rive r sim ul a ti o n .
#


class Gender(Enum):
    FEMALE = 1
    MALE = 2


class Animal(ABC):
    # Create an animal of the specified age and gender .
    # If no age and gender are passed, then create
    # an animal of a random age and gender.
    def __init__(self, age=None, gender=None):
        if gender is None:
            self.gender = Gender.FEMALE if random.randint(0, 1) == 0 \
                else Gender.MALE
        else:
            self.gender = gender
        self.age = age

# Returns true if the current age of the animal
# has reached the limit for the species .
# Otherwise, it returns false .
    @abstractmethod
    def maxAge():
        pass

# Get the age of the animal.
    @abstractmethod
    def getAge():
        pass

# If the current age of the animal is less than the maximum
# for the species, increments the age of the animal by one
# and returns true.

    @abstractmethod
    def incrAge():
        pass

    @abstractmethod
    def getGender():
        pass