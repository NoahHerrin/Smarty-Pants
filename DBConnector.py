from SimpleDB import MongoDB as DB

def connect(Collection, Properties):
    return DB.Database("herrinn", "root123", "smarty-pants", Collection, Properties)
