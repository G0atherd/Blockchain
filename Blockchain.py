import datetime
import hashlib
from colorama import Fore, Back, Style

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha512()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return '\033[36m'+" Tiko Hash: " + str(self.hash()) + "\Tiko: " + str(self.blockNo) + "\nTiko Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20 
    maxNonce = 2**32
    target = 2 ** (512-diff)
    target1 = target ** 2 * (512-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target1:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(100):
    blockchain.mine(Block('\033[36m' +" Tiko:" + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next