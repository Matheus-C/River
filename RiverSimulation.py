from River import *

# verify the type of entry: 1 - random, 2 - file with a starting river, 3 - exit the program
typeOfEntry = None
while typeOfEntry != "3":
    typeOfEntry = input("Enter 1 to generate a random, 2 for to add an file entry or 3 to exit")
    while typeOfEntry != "1" and typeOfEntry != "2" and typeOfEntry != "3":
        print("Error, enter a valid option")
        typeOfEntry = input("Enter 1 to generate a random, 2 for to add an file entry or 3 to exit")
    # random river
    if typeOfEntry == "1":
        size = input("Enter the size of the river")
        while int(size) < 1:
            print("Error, only positive numbers please")
            size = input("Enter the size of the river")
        river = River(int(size))
        river.generateRandom()
    # river from a file
    elif typeOfEntry == "2":
        file = input("enter the path of the file")
        river = River(file)
    else:
        # exit when typeOfEntry == 3
        quit()

    numberOfCycles = input("enter the number of cycles")
    while int(numberOfCycles) < 1:
        print("Error, only positive values are accepted")
        numberOfCycles = input("enter the number of cycles")
    print("Initial River")
    print(river)
    print()
    # update the river for each cycle
    for i in range(1, int(numberOfCycles)+1, 1):
        river.updateRiver()
        print("After cycle", i)
        print(river)
        print()
    
