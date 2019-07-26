class Item(object):
    def __init__(self):
        self.__vertexId = None
        self.__properties = {}

    def modifyProperty(self, property, newValue):
        self.__properties[property] = newValue
    
    def getProperty(self, property):
        if property in self.__properties:
            return self.__properties[property]
        raise Exception("Property '{}' doesn't exist".format(property))
    
    def debugItem(self):
        print("vertex id", self.__vertexId)
        for property in self.__properties:
            print(property, self.__properties[property])