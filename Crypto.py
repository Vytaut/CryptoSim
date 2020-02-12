import Blockchain as bc
import Block as bl


class Crypto:

    def __init__(self, chain: bc.BlockChain):
        self.chain = chain

    def validateChain(self):
        for i in range(1, len(self.chain.blockChain)):
            block = self.chain.blockChain[i]
            if not block.validateBlock() or not self.chain.validateBlockSeq(self.chain.blockChain[i-1],block):
                return False
        return True
