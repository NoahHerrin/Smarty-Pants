from Modules.Closet.Item import Item


## -------------------------------------------------------------------------- ##
## object: Catagory
## purpose: a datastructure to manipulate and organize multiple Item objects
## methods: addItem, getItems, display_items, setNextCatagory, getNextCatagory
##          getPreviousCatagory, setPreviousCatagory, printCatagory, getName
## variables: __catagoryName, __listOfItems, __numItems, __nextCatagory,
##            __previousCatagory
## -------------------------------------------------------------------------- ##

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

    ## -------------------------------------------------- ##
    ## function: getItems
    ## purpose: gets a list of all items in the catagory
    ## returns: a list of item objects or None if
    ##          catagory is empty
    ## -------------------------------------------------- ##

    def getItems(self):
        if self.__numItems == 0:
            return None
        else:
            return self.__listOfItems


    def display_items(self):
        for item in self.__listOfItems:
            item.debugItem()

    def setNextCatagory(self, nextCatagory):
        self.__nextCatagory = nextCatagory 

    def getNextCatagory(self):
        return self.__nextCatagory 

    def setPreviousCatagory(self, previous):
        self.__previousCatagory = previous

    def getPreviousCatagory(self):
        return self.__previousCatagory

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
    
    ## ----------------------------------------------------------- ##
    ## function: formatCatagoryForSave
    ## purpose: formats items in catagory to be saved
