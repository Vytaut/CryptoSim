import hashlib

class Block:

    def __init__(self,index,timestamp,data,prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.calculateHash()

    def calculateHash(self):
        hash = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prevhash)
        return hashlib.sha256(hash.encode())

#TODO: genesis block