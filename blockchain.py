import hashlib  # bytes like info
import datetime  # timezone info
import json  # block format
from hashlib import sha256  # bytes like info


class Blockchain():

    def __init__(self):
        self.chain = []
        self.pending_chain = []
        self.add_block(nonce=1, prev_hash="0")

    def add_block(self, nonce, prev_hash=None):  # move to actual blockchain after getting approved
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'transaction': self.pending_chain,
                 'nonce': nonce,
                 'previous_hash': prev_hash or self.hash(self.chain[-1])}

        self.pending_chain = []
        self.chain.append(block)

        return block

    def add_data(self, transaction):  # new work
        self.pending_chain.append(transaction)

    def get_prev_block(self):
        return self.chain[-1]

    def new_data(self, voter, candidate):
        data = {
            'voter': voter,
            'candidate': candidate,
        }
        self.add_data(data)
        return self.chain[-1]['index'] + 1  # index of new block

    def hash(self, block):
        string = json.dumps(block, sort_keys=True)  # convert object to json
        newblock = string.encode()
        hash = sha256(newblock).hexdigest()
        return hash

    def hash_operation(self, nonce, previous_nonce):
        return sha256(str(nonce ** 2 - previous_nonce ** 2).encode()).hexdigest()

    def proof_of_work(self, prev_nonce):

        nonce_valid = False
        nonce = 1

        while nonce_valid is False:
            nonce_hash = self.hash_operation(nonce, prev_nonce)

            if nonce_hash.startswith('0'):
                nonce_valid = True
            else:
                nonce = nonce + 1
        return nonce

    def is_valid(self, chain):
        prev_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(prev_block):
                return False

            prev_nonce = prev_block['nonce']
            current_nonce = block['nonce']
            nonce_hash = self.hash_operation(current_nonce, prev_nonce)
            if nonce_hash[:1] == '0':
                return False

            prev_block = block
            block_index = block_index + 1

        return True