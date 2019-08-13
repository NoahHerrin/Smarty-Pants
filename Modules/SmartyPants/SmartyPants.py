# acts as an interface for the graph algorithmn and the clothing item data represented by the algorithmn
import Catagory as catagory
import Item as item

class SmartyPants(object):

    def __init__(self):
        self.__closet = {}

    def addCatatagory(self, CatagoryName):
        if CatagoryName not in self.__closet:
            self.__closet[CatagoryName] = catagory.Catagory()
        else:
            print("Catagory {} already exists.".format({CatagoryName}))
    
    def addItem(self, Catagory, newItem=None, VertexId=None, Name=None):
        
        if newItem is None:
            newItem = item.Item(VertexId, Name)
        # check if item is going in to a new Catagory, if so create new catagory
        if Catagory not in self.__closet:
            self.addCatatagory(Catagory)
        
        self.__closet[Catagory].append(newItem)
        
    # prints information about each item in the closet
    def printCloset(self):
        for catagory in self.__closet:
            print(catagory)
            # iterate through the list of items
            for item in self.__closet[catagory]:
                item.debugItem()