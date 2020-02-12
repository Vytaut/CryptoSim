import Blockchain as bc
import Block as bl


class Crypto:

    def __init__(self, chain: bc.BlockChain):
        self.chain = chain

    def validateChain(self):
        #TODO: validate genesis block
        for i in range(1, len(self.chain.blockChain)):
            if not self.chain.blockChain[i].validateBlock() or not self.chain.validateBlockSeq(self.chain.blockChain[i-1],self.chain.blockChain[i]):
                return False
        return True

    def replaceChain(self,newChain: bc.BlockChain):
        if len(self.chain.blockChain) < len(newChain.blockChain):
            print('Replaced old chain with longer one')
            self.chain = newChain
        else:
            print('New chain invalid')
