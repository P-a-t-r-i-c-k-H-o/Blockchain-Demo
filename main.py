from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

t1 = blockchain.new_data("Tommy S", "Tommy")
t2 = blockchain.new_data("JP", "Andre")
t3 = blockchain.new_data("Dr. B", "Pat")
blockchain.add_block(12)

t4 = blockchain.new_data("Joe", "Biden")
t5 = blockchain.new_data("Barack", "Obama")
t6 = blockchain.new_data("Updog", "Underthere")
blockchain.add_block(15)


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = blockchain.chain
    return jsonify(response), 200


@app.route('/verify_block', methods=['GET'])
def verify_block():
    prev_block = blockchain.get_prev_block()
    prev_nonce = prev_block['nonce']
    proof = blockchain.proof_of_work(prev_nonce)
    prev_hash = blockchain.hash(prev_block)

    block = blockchain.add_block(proof, prev_hash)
    response = {'message': 'Complete',
                'index' : block['index'],
                'timestamp': block['timestamp'],
                'nonce': block['nonce'],
                'prev_hash': block['previous_hash']}
    return jsonify(response), 200

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)







