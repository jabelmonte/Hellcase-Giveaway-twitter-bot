class Keys():

    # def __init__(self):

    def getKeys(self):
        filepath = "../keys/keys.txt"
        #reader
        with open(filepath, 'r') as file:
            pullKeys = file.read().splitlines()
            allKeys = {
                "a": pullKeys[0],
                "b": pullKeys[1],
                "c": pullKeys[2],
                "d": pullKeys[3]
            }
           
        file.close()
        return allKeys