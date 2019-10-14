
## ------------------------------------------------------##
## object: Item
## purpose: A datastructure for storing item data
## methods: getName, getVertexId, modifyProperty, 
##          getProperties, getProperty, debugItem
##          hasSameProperties
## variables: __vertexId, __properties
## ------------------------------------------------------##

class Item(object):
    
    def __init__(self, vertexId, Name):
        self.__vertexId = vertexId
        self.__properties = {'name': Name}


    ## ------------------------------------------------ ##  
    ## function: getName
    ## purpose: to get the name of the item
    ## returns: a string name of an item
    ## ------------------------------------------------ ##  

    def getName(self):
        return self.__properties['name']


    ## ------------------------------------------------ ##  
    ## function: getName
    ## purpose: gets id for a vertex in a graph
    ## returns: an integer id
    ## ------------------------------------------------ ##  

    def getVertexId(self):
        return self.__vertexId
    

    ## ------------------------------------------- ##
    ## function: modifyProperty
    ## purpose: adds or changes a item property
    ## parameters: property, newValue
    ## ------------------------------------------- ##

    def modifyProperty(self, property, newValue):
        self.__properties[property] = newValue


    ## --------------------------------------------------------- ##
    ## function: getProperties
    ## purpose: gets all item properties
    ## returns: a dictionary containing properties for the item
    ## --------------------------------------------------------- ##    

    def getProperties(self):
        return self.__properties


    ## ------------------------------------------------------------ ##
    ## function: getProperty
    ## purpose: returns the property stored for a specific property
    ## parameters: property
    ## returns: value of a property
    ## ------------------------------------------------------------ ##

    def getProperty(self, property):
        if property in self.__properties:
            return self.__properties[property]
        raise Exception("Property '{}' doesn't exist".format(property))
    

    ## ------------------------------------------------------------ ##
    ## function: debugItem
    ## purpose: prints the name, id, and all properties of an item
    ## ------------------------------------------------------------ ##

    def debugItem(self):
        print("\tvertex id", self.__vertexId)
        for property in self.__properties:
            print("\t{} {}".format(property, self.__properties[property]))
    

    ## ------------------------------------------------------------ ##
    ## function: hasSameProperties
    ## purpose: to check that items contain the same properties
    ## returns: a boolean that represents whether both items
    ##          have the same properties
    ## ------------------------------------------------------------ ##

    def hasSameProperties(self, other):
        if len(self.__properties) != len(other.getProperties()):
            return False
        else:
            otherProps = other.getProperties()
            for property in self.__properties:
                if property not in otherProps:
                   return False
            return False

    ## ------------------------------------------------------------- ##
    ## function: formatForSave
    ## purpose: convert item data to a string that
    ##          can be stored in memory.
    ## returns: a string version of this item
    ## notes: format for item saving
    ##        propertyname=propertyvalue, nextproperty=nextpropertyvalue,...
    ## ------------------------------------------------------------- ##

    def formatForSave(self):
        retVal = "VertexId={},".format(self.__vertexId)

        for property in self.__properties:
            retVal += "{}={},".format(property, self.__properties[property])
        return retVal + "\n"
        
