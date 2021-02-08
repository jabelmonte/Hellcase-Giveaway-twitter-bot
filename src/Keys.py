class Keys():

    # def __init__(self):

    def getKeys(self):
        filepath = "../keys/keys.txt"
        #reader
        with open(filepath, 'r') as file:
            pullKeys = file.read().replace('\n ', '')
            storedKeys = pullKeys
        file.close()
        return storedKeys