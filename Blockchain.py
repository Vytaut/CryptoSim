import time

import Block as bl


class BlockChain:
    def __init__(self):
        self.blockChain: [bl.Block] = [self.generateGenesisBlock()]

    def generateGenesisBlock(self):
        return bl.Block(0, time.time(), None, None)

    def generateNextBlock(self, blockdata: str):
        prevblock = self.getLastBlock()
        index = prevblock.index + 1
        prevhash = prevblock.calculateHash()
        return bl.Block(index, time.time(), blockdata, prevhash)

    def getLastBlock(self):
        return self.blockChain[-1]

    def validateBlockSeq(self, prevblock: bl.Block, nextblock: bl.Block):
        if prevblock.index + 1 != nextblock.index:
            print('Invalid block index!')
            return False
        if prevblock.calculateHash() != nextblock.prevhash:
            print('Invalid previous block hash!')
            return False
        if nextblock.calculateHash() != nextblock.hash:
            print('Invalid block hash!')
            return False
        return True