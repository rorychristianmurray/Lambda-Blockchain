import hashlib
import requests

import sys
import json

DIFFICUTLY = 3

def proof_of_work(self, block):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    # turns the last block into a json string
    # with the keys sorted (to maintain integrity of hash)
    block_string = json.dumps(self.last_block, sort_keys=True)

    # start looking for proof at zero
    proof = 0

    # run while loop and iterate until made enough
    # guesses to stumble on answer, iterating up by 
    # 1 each time
    while self.valid_proof(block_string, proof) is False:
        proof += 1

    # when find valid proof to make the hash work
    # return it
    return proof
    


def valid_proof(block_string, proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """

    # create guess by combining block_string and proof
    # and encoding as bytes
    guess = f'{block_string}{proof}'.encode()

    # hash guess to get hexidecimal representation
    guess_hash = hashlib.sha256(guess).hexdigest()

    # return boolean if guess hashed with specified
    # amount of nonce values
    return guess_hash[:DIFFICULTY] == "0" * DIFFICULTY

    


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # Load ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # Run forever until interrupted
    while True:
        r = requests.get(url=node + "/last_block")
        # Handle non-json response
        try:
            data = r.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break

        # TODO: Get the block from `data` and use it to look for a new proof
        # new_proof = ???

        # When found, POST it to the server {"proof": new_proof, "id": id}
        post_data = {"proof": new_proof, "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()

        # TODO: If the server responds with a 'message' 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
