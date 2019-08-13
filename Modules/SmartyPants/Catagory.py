from Item import Item

class Catagory(object):
    def __init__(self):
        self.__listOfItems = []
        self.__numItems = 0
        self.__nextCatagory = None
        self.__previousCatagory = None

    def addItem(self, newItem):
        self.__listOfItems.append(newItem)
        self.__numItems += 1

    def display_items(self):
        for item in self.__listOfItems:
            item.debugItem()

    def setNextCatagory(self, next):
        self.__nextCatagory = next

    def getNextCatagory(self):
        return self.__nextCatagory 

    def setPreviousCatagory(self, previous):
        self.__previousCatagory = previous

    def getPreviousCatagory(self):
        return self.__nextCatagory