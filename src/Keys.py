class Keys():

    # def __init__(self):

    def getKeys(self):
        filepath = "../keys/keys.txt"
        #reader
        with open(filepath, 'r') as file:
            pullKeys = file.read().replace('\n ', '')

        file.close()
        print(pullKeys)