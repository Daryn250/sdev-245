'''In this project, students will create a small application or script that:

Accepts user input (e.g., a message or file)
Hashes the input using SHA-256 to ensure integrity
Encrypts the input using symmetric encryption (e.g., AES)
Decrypts the content and verifies its integrity via hash comparison
2. Students must also:

Write a short explanation describing how their solution upholds confidentiality, integrity, and availability
Explain the role of entropy and key generation in their implementation'''

# accept input

text = input("Enter a string to be encrypted! \n")


# hash input using sha256

import hashlib # expert python imports here only

def hash_that_thing(thing):
    hash_obj = hashlib.sha256(thing.encode('utf-8')) # encode the input with utf8 first to make sure no funny business, and then encrpyt it with hashlib
    hex_dig = hash_obj.hexdigest() # we'll use this later in our code
    return hex_dig

# encrypt with symmetric encryption

from cryptography.fernet import Fernet # type: ignore
import os
import base64

fernet_key = base64.urlsafe_b64encode(os.urandom(32)) # change this with a consistent password if you want to be able to decode text later on
f = Fernet(fernet_key)


def encrypt(message):
    # finally encrypt
    secret_message = message.encode('utf-8')
    encrypted = f.encrypt(secret_message)

    return encrypted

def decrypt(encrypted):

    decrypted = f.decrypt(encrypted)
    return decrypted.decode()

# verify integrity
original_hash = hash_that_thing(text)

encrypt_it = encrypt(text)

print(original_hash, '\n', encrypt_it)

decrypt_it = decrypt(encrypt_it) # for the longest time, it was set as text instead of the encrypted text. this is an awful typo

final_hash = hash_that_thing(decrypt_it)

print(final_hash, '\n', decrypt_it)

if original_hash == final_hash:
    print("HASHES MATCH, VERIFIED")

else:
    print("HASHES DO NOT MATCH")


# write explanation

'''
Write a short explanation describing how their solution upholds confidentiality, integrity, and availability
Explain the role of entropy and key generation in their implementation

My solution upholds confidentiality by assuring that only someone with this script can encode and decode any given data. It also makes sure that data put in to be encrypted, when decrypted, is assuredly not tampered with.
It upholds integrity by keeping data stored secure, even if it were to fall into the hand of a malicious force. And finally, since this script can be run locally
it assures that the data is kept available at all times.

Entropy and key generation in my code keeps my data secure. Entropy creates the 32 bit key that allows for encryption and decryption of data. It's randomly generated as of now, and could theoretically be increased 
until cryptography's fernet algorithm hits its limit. Entropy ensures that if I generated a large number of keys, there should be little to no overlap.
'''