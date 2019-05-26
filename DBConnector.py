from SimpleDB.MongoDB import Database




def connect(collection,data):
    return Database("herrinn", "root123", "smarty-pants", collection, data)
