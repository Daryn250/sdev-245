# pro gramming again 

import random



class asymmetric:
    def __init__(self, base, prime, set_key = None):
        self.priv_key = random.randint(2,100) if set_key == None else set_key # this is extremely bad practice. works for an example. use sha256
        self.base = base # base for exponent
        self.prime = prime # prime for exponent
        self.pub_key = pow(self.base, self.priv_key, self.prime) # calculate public key based from private key

    def compute_secret(self, public): # compute the secret based off another person's public key and my private key
        self.secret = pow(public, self.priv_key, self.prime)
        return self.secret
    
def encrypt(message, secret): # encrypt a message badly. it's just converting to ascii and then multiplying by the secret number. this isn't secure.
    e = [] # list
    for i in range(len(message)):
        e.append(ord(message[i])*secret+1) # change to ascii, multiply by secret, add 1
    
    m = ""
    for i in e:
        m += chr(i) # change back to characters
    
    return m

def decrypt(message, secret):
    e = [] # list
    for i in range(len(message)):
        e.append(ord(message[i])/secret) # change to ascii, divide by secret
    
    m = ""
    for i in e:
        m += chr(round(i)) # change to characters
    
    return m
    

base, prime = 5, 29 # should be picked at random and should use larger primes. oh well :)


alice_key = asymmetric(base, prime, 5)
bob_key = asymmetric(base, prime, 62)

print(f"Asymmetric: Alice Private Key: {alice_key.priv_key}, Bob Private Key: {bob_key.priv_key}")
print(f"Shared Secrets: Alice - {alice_key.compute_secret(bob_key.pub_key)}, Bob - {bob_key.compute_secret(alice_key.pub_key)}")

message = "Hello Bob, it's me Alice!"
message = encrypt(message, alice_key.secret)

print(f"Encrypted: {message}")

decrypted = decrypt(message, bob_key.secret)

print(f"Decrpyted: {decrypted}")

print("\n Symmetric Key Example:")

# symmetric key encryption example:

message = "This is a string of characters to be encrypted and decrypted."
random_number = random.randint(1, 10000) # terrible key selection lol

message = encrypt(message, random_number)

print(f"Encrypted: {message}")

decrypted = decrypt(message, random_number)

print(f"Decrpyted: {decrypted}")

print(f"Key: {random_number}")