from Modules.SmartyPants.Item import Item

class Catagory(object):
    def __init__(self, name):
        self.__catagoryName = name
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
    def getName(self):
        return self.__catagoryName
    ## ------------------------------------------------------------------------- ##
    ## function: printCatagory
    ## purpose: prints out each item stored within the catagory in a neat table
    ##          for debugging purposes
    ## ------------------------------------------------------------------------- ##

    def printCatagory(self):
        # title
        print("Catagory: {}".format(self.__catagoryName))

        # catagory details
        print("\tItem #: {}".format(self.__numItems))

        if self.__nextCatagory is None:
            print("\tNext Catagory: NULL")
        else: 
            print("\tNext Catagory: {}".format(self.__nextCatagory.getName()))

        if self.__previousCatagory is None:
            print("\tPrevious Catagory: NULL")
        else: 
            print("\tPrevious Catagory: {}".format(self.__previousCatagory.getName()))
        

        # print catagory items
        if(self.__numItems == 0):
            print("\tcatagory is empty, double check code to see if this catagory is a mistake")
        else:

            for item in self.__listOfItems:
                print("\tItem: (name = {}, id = {})".format(item.getName(), item.getVertexId()))