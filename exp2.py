import datetime
import hashlib
import json
from flask import Flask, jsonify

# --- PART 1: BLOCKCHAIN LOGIC ---

class Blockchain:
    def __init__(self):
        self.chain = []
        # Create the genesis block
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        """Creates a new block and adds it to the chain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        """Returns the SHA-256 hash of a block."""
        # sort_keys=True ensures the hash is consistent every time
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, previous_proof):
        """
        The Mining Algorithm: 
        Find a number 'p' such that hash(p^2 - prev_p^2) starts with 0000.
        """
        new_proof = 1
        while True:
            hash_operation = self._calculate_pow_hash(new_proof, previous_proof)
            if hash_operation.startswith('0000'):
                return new_proof
            new_proof += 1

    def is_chain_valid(self):
        """Validates the entire blockchain integrity."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # 1. Check if the link is broken
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # 2. Check if the Proof of Work is valid
            pow_hash = self._calculate_pow_hash(current_block['proof'], previous_block['proof'])
            if not pow_hash.startswith('0000'):
                return False
                
        return True

    @staticmethod
    def _calculate_pow_hash(new_proof, previous_proof):
        """Helper to calculate SHA-256 for the PoW math puzzle."""
        formula = str(new_proof**2 - previous_proof**2).encode()
        return hashlib.sha256(formula).hexdigest()

# --- PART 2: WEB API ---

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    last_block = blockchain.get_last_block()
    proof = blockchain.proof_of_work(last_block['proof'])
    previous_hash = blockchain.hash(last_block)
    
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'Congratulations, you just mined a block!',
        **block  # Cleaner way to include all block keys in the response
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }), 200

@app.route('/is_valid', methods=['GET'])
def check_validity():
    is_valid = blockchain.is_chain_valid()
    message = "All good. The Blockchain is valid." if is_valid else "We have a problem. Chain is invalid."
    return jsonify({'message': message, 'is_valid': is_valid}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)