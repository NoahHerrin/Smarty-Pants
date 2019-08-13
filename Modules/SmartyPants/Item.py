class Item(object):
    def __init__(self, vertexId, Name):
        self.__vertexId = vertexId
        self.__properties = {}
        self.__properties = {'name': Name}
        
    def getName(self):
        return self.__properties['name']
    def modifyProperty(self, property, newValue):
        self.__properties[property] = newValue

    def getProperties(self):
        return self.__properties
    def getProperty(self, property):
        if property in self.__properties:
            return self.__properties[property]
        raise Exception("Property '{}' doesn't exist".format(property))
    
    def debugItem(self):
        print("vertex id", self.__vertexId)
        for property in self.__properties:
            print(property, self.__properties[property])
    
    # will be used to recursively evaluate the 
    def hasSameProperties(self, other):
        if len(self.__properties) != len(other.getProperties()):
            return False
        else:
            otherProps = other.getProperties()
            for property in self.__properties:
                if property not in otherProps:
                   return False
            return False
