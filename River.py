from Animal import *
from Bear import *
from Fish import *


class River(object):
    # If arg is a string, then it will be the inputFileName,
    # and the river will be constructed from a file.
    # If arg is an integer, then it will be the length of the river.
    # May raise IOError.
    def __init__(self, arg=0):
        self.river = []  # list of animals

        if type(arg) == str:
            try:
                file = open(arg, "r")
                self.length = int(file.readline())# first line is the length of the river
                fileRiver = file.readline().split()# read the line with the starting river
                for i in range(len(fileRiver)):
                    if fileRiver[i][0] == "B":
                        if fileRiver[i][1] == "F":
                            animalType = ("BF")
                        else:
                            animalType = ("BM")
                    elif fileRiver[i][0] == "F":
                        if fileRiver[i][1] == "F":
                            animalType = ("FF")
                        else:
                            animalType = ("FM")
                    else:
                        animalType = None
                    if animalType == "BF":
                        self.river.append(Bear(int(fileRiver[i][2]), Gender.FEMALE))
                    elif animalType == "BM":
                        self.river.append(Bear(int(fileRiver[i][2]), Gender.MALE))
                    elif animalType == "FF":
                        self.river.append(Fish(int(fileRiver[i][2]), Gender.FEMALE))
                    elif animalType == "FM":
                        self.river.append(Bear(int(fileRiver[i][2]), Gender.MALE))
                    else:
                        self.river.append(None)
            except:
                print("error with reading")
        else:
            self.length = arg  # The length of the river(number of cells).

    # Returns the length of the river
    def getLength(self):
        return len(self.river)

# Returns the number of empty ( None ) cells in the river.

    def numEmpty(self):
        counter = 0
        for i in range(self.getLength()):
            if self.river[i] == None:
                counter += 1
        return counter

    # Generates a random river cell
    def generateRandom(self):
        options = ["Bear", "Fish", "None"]
        for i in range(self.length):
            chosen = random.choice(options)
            if chosen == "Bear":
                bear = Bear()
                self.river.append(bear)
            elif chosen == "Fish":
                fish = Fish()
                self.river.append(fish)
            else:
                self.river.append(None)


# If the river has no empty (None) cells, then do nothing
    # and return False.
    # Otherwise, add an animal of age 0 of randomly chosen
    # gender and of the same type as animal to a cell chosen
    # uniformly at random from among the currently empty cells
    # and return True .


    def addRandom(self, animal):
        if self.numEmpty() != 0:
            place = random.randint(0, self.numEmpty())
            count = 0
            for i in range(len(self.river)):
                if self.river[i] == None:
                    if count == place:
                        if animal == "Bear":
                            self.river[i] = Bear(0)
                        else:
                            self.river[i] = Fish(0)
                        break
                    else:
                        count += 1
        else:
            return False

    # Process the object at cell i, following the rules given in
    # the Project Description. If it is None, do nothing.
    # decides which direction, if any, the animal
    # should move, and what other actions to take
    # (including the creation of a child),
    # following the rules given in the Project Description.
    def updateCell(self, i):
        if self.river[i] is not None:
            if not self.river[i].incrAge():
                print(type(self.river[i]).__name__ +
                      " on position "+str(i)+" dies")
                self.river[i] = None  # die
        if self.river[i] == None:
            pass
        else:
            if type(self.river[i]).__name__ == "Bear":
                animalType = "Bear"
            else:
                animalType = "Fish"

            actions = ["none"]# list of possible actions, starts with none and will be filled with possible options.
            if i < 1:
                if type(self.river[i]).__name__ == type(self.river[i + 1]).__name__ and self.river[i + 1].getGender() != self.river[i].getGender() and self.numEmpty() > 0:
                    actions.append("mate")
                else:
                    if animalType == "Bear":
                        if type(self.river[i + 1]).__name__ == "Fish":
                            actions.append("feed_right")
                        else:
                            actions.append("fight_right")
            elif i == len(self.river)-1:
                if type(self.river[i]).__name__ == type(self.river[i - 1]).__name__ and self.river[i - 1].getGender() != self.river[i].getGender() and self.numEmpty() > 0:
                    actions.append("mate")
                else:
                    if animalType == "Bear":
                        if type(self.river[i - 1]).__name__ == "Fish":
                            actions.append("feed_left")
                        else:
                            actions.append("fight_left")
            else:
                if type(self.river[i]).__name__ == type(self.river[i + 1]).__name__:
                    if self.river[i + 1].getGender() != self.river[i].getGender() and self.numEmpty() > 0:
                        actions.append("mate")
                    elif self.river[i - 1].getGender() != self.river[i].getGender() and self.numEmpty() > 0:
                        actions.append("mate")

                if animalType == "Bear":
                    if type(self.river[i + 1]).__name__ == "Fish":
                        actions.append("feed_right")
                    elif type(self.river[i + 1]).__name__ == "Bear" and self.river[i+1].getGender() == self.river[i].getGender():
                        actions.append("fight_right")
                    if type(self.river[i - 1]).__name__ == "Fish":
                        actions.append("feed_left")
                    elif type(self.river[i - 1]).__name__ == "Bear" and self.river[i-1].getGender() == self.river[i].getGender():
                        actions.append("fight_left")
                #now the list of possible actions is filled and 1 will be selected randomly and that action is taken
                selectAction = random.randint(0, len(actions)-1)
                if actions[selectAction] == "feed_left":
                    self.river[i-1] = None
                    print(animalType + " on position " +
                          str(i)+" feeds on Fish on the left")
                elif actions[selectAction] == "feed_right":
                    self.river[i+1] = None
                    print(animalType + " on position " +
                          str(i)+" feeds on Fish on the right")
                elif actions[selectAction] == "fight_left":
                    if self.river[i].getStrength() >= self.river[i-1].getStrength():
                        self.river[i-1] = None
                        print(animalType + " on position "+str(i) +
                              " fights another "+animalType+" on the left and wins")
                    else:
                        print(animalType + " on position "+str(i) +
                              " fights another "+animalType+" on the left and loses")
                        self.river[i] = None
                elif actions[selectAction] == "fight_right":
                    if self.river[i].getStrength() >= self.river[i+1].getStrength():
                        self.river[i+1] = None
                        print(animalType + " on position "+str(i) +
                              " fights another "+animalType+" on the right and wins")
                    else:
                        self.river[i] = None
                        print(animalType + " on position "+str(i) +
                              " fights another "+animalType+" on the right and loses")
                elif actions[selectAction] == "mate":
                    self.addRandom(animalType)
                    print(animalType + " on position "+str(i) +
                          " mates with another "+animalType)
            directions = []# list of possible directions
            move = random.randint(0, 1)# decides if it will move to another cell
            if move == 1:
                if i == 0:
                    if self.river[i + 1] == None:
                        directions.append("right")
                elif i == len(self.river)-1:
                    if self.river[i - 1] == None:
                        directions.append("left")
                else:
                    if self.river[i + 1] == None:
                        directions.append("right")
                    if self.river[i - 1] == None:
                        directions.append("left")

                if directions != []:
                    moveTo = random.randint(0, len(directions)-1)# if the animal decides to move, then the direction is selected randomly of the possible ones
                    if directions[moveTo] == "right":
                        print(animalType + " on position " +
                              str(i)+" moves to the right")
                        self.river[i + 1] = self.river[i]
                        self.river[i] = None
                    elif directions[moveTo] == "left":
                        print(animalType + " on position " +
                              str(i)+" moves to the left")
                        self.river[i - 1] = self.river[i]
                        self.river[i] = None

    # Perform one cycle of the simulation , going through
    # the cells of the river, updating ages, moving animals,
    # creating animals, and killing animals, as explained
    # in the Project Description.
    def updateRiver(self):
        for i in range(self.getLength()):
            self.updateCell(i)
            

    # Write the river to an output file.
    # May raise IOError.
    def write(self, outputFileName):
        pass

 # Produce a string representation of the river.
    def __repr__(self):

        riverStr = ""
        for i in range(self.getLength()):
            riverStr += ("_" * 3) \
                if self.river[i] is None else str(self.river[i])
            if i < self.getLength() - 1:
                riverStr += " "
        return riverStr
