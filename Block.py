import hashlib


class Block:

    def __init__(self,index: int,timestamp: float,data: str,prevhash: hex):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.calculateHash()

    def calculateHash(self):
        hash = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prevhash)
        return hashlib.sha256(hash.encode()).hexdigest()

    def validateBlock(self):
        if self.index != 0:
            return type(self.index) == 'int' and \
                   type(self.timestamp) == 'float' and \
                   type(self.data) == 'str' and \
                   type(self.prevhash) == 'hex' and \
                   type(self.hash) == 'hex'
        return True
