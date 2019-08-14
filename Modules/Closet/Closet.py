# acts as an interface for the graph algorithmn and the clothing item data represented by the algorithmn
import Modules.Closet.Catagory as catagory
import Modules.Closet.Item as item

class Closet(object):

    def __init__(self):
        self.__closet = {}

        # create catagories
        pants = self.addCatagory('pants')
        shoes = self.addCatagory('shoes')
        shirts = self.addCatagory('shirt')
        layer = self.addCatagory('layer')

        # set up catagory relations
        shoes.setNextCatagory(pants)
        pants.setPreviousCatagory(shoes)
        pants.setNextCatagory(shirts)
        shirts.setPreviousCatagory(pants)
        shirts.setNextCatagory(layer)
        layer.setPreviousCatagory(shirts)
        
        



    def addCatagory(self, CatagoryName):
        if CatagoryName not in self.__closet:
            self.__closet[CatagoryName] = catagory.Catagory(CatagoryName)
            return self.__closet[CatagoryName]
        else:
            print("Catagory {} already exists.".format({CatagoryName}))

    ## ---------------------------------------------------------- ##
    ## function: getCatagory
    ## purpose: used by interface to access individual catagories
    ## parameter: catagoryName
    ## returns: Catagory object with coorisponding catagoryName
    ##          or None if no such catagory exists
    ## ---------------------------------------------------------- ##
    
    def getCatagory(self, catagoryName):
        name = catagoryName.lower()

        # confirm that catagory exists
        if name not in self.__closet:
            return None
        else:
            return self.__closet[name]

    def addItem(self, Catagory, newItem=None, VertexId=None, Name=None):
        
        if newItem is None:
            newItem = item.Item(VertexId, Name)
        
        # convert catagory to lowercase and check if catagory already exists
        Catagory = Catagory.lower()
        if Catagory not in self.__closet:
            self.addCatagory(Catagory)
        
        self.__closet[Catagory].addItem(newItem)
        
    # prints information about each item in the closet
    def printCloset(self):
        print("\nPrinting Closet Contents")
        for catagory in self.__closet:
            self.__closet[catagory].printCatagory()
            print("")
            
            