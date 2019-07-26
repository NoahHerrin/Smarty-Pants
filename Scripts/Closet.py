from Item import Item

class Catagory(object):
    def __init__(self):
        self.__listOfItems = []
        self.__numItems = 0

    def addItem(self, newItem):
        self.__listOfItems.append(newItem)
        self.__numItems += 1