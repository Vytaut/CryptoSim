import hashlib

class Block:

    def __init__(self,index,timestamp,data,hash,prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.prevHash = prevhash

    def calculateHash(self,index,timestamp,data,prevhash):
        hash = str(index) + str(timestamp) + str(data) + str(prevhash)
        return hashlib.sha256(hash.encode())