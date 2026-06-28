#Write an app that generates SHA-256 hashes for input strings or files

import hashlib
import os

target = "Hello World"

# check if the target is a file rq
if os.path.isfile(target):
    target_is_file = True
else:
    target_is_file = False


# turn into single string
if target_is_file:
    with open(target, "r", encoding="utf-8") as file:
        content = file.read()
else:
    content = target

# use hashlib to turn into a hash
hash_obj = hashlib.sha256(content.encode("utf-8"))
hex_digest = hash_obj.hexdigest()
print(hex_digest)


# part 2
#Write an app that uses a simple substitution cipher (Caesar cipher or similar) to encrypt/decrypt input text

content # the unencrpyted data (you dont have to modify the data to write it in a line like this (expert programmer (me (sarcasm))))
encrypted = ""
decrypted = ""

for letter in content:
    ascii = ord(letter)
    ascii += 2 # hardcoded
    encrypted+=chr(ascii)

print(encrypted)

for letter in encrypted:
    ascii = ord(letter)
    ascii -= 2 # hardcoded again because why not
    decrypted += chr(ascii)

print(decrypted)


# part 3
#Use OpenSSL or a tool to simulate a digital signature (sign/verify).
generated_private_key_with_openssl = '''
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCV4i9cjAQtUkIA
cnBRs62IVgG0x1sqPi09ucHxDb1XTk2FZYCz4DBjc31bZDAtzNZ0M2XGxBxzfLWQ
g8vKcIwFuphy0P7h+WKEz4fyTZAeBafScoebFIvvvMLb9MgAi1KqRyHS8LnlYQx0
sOlTt3T5X5P80LUNR5SFrGzFSykqhivq+0XchvFwi6AjHq00rBiv9P5E+EESLwZn
wl3nRo75pYBMBZDCLY0zOg9tfrPhaientlc5WPPj0U/07U80hCtY79nWzYImoUAC
EyzAEfkz+fRmYUH6ANxJKFpQh15bgdeLd19KvdXSFzd3m0ePM2w4FAuu9ngmS8FL
w0RB875lAgMBAAECggEABz/o2dTmfxuNqrcneBHr3ln1fHQVgkUQorTBXzuyineZ
MQXzxDZodVXbE5iCM8hZIJApTCkAVd35RxyukkOk7HkoRBzhWqRZlqI61zQggg2G
+i2Jj7+nUEHilYl1i+5Vz6A7UBhORrNgFDdsZS9M1X4uyqKhZ0Aac1WfpqlX8sEI
rXv9zXMf7tj1axUn2P1iRzHjYyTupEONhd9N5eAoMKF8NZOG7HprgaC6CdD3Yo6W
WKNsLU9HklMuO83i3FUeEt4BeIDLyEOgdxo7YTz/OfdbN7mEBx2JActmthD0c9jX
NBHRv5Gu4gi4cORg6YcF7jm52UQVNNlFRHKILLFlbwKBgQDHKMJKOR8ku/fAReWo
WMREdSeLi31vyKhmF5OUuf5H1VzrWTbUrJRDEhdY7Jg2y6Poh6tATTUAdizJjbZz
kE+xLbdct9X2qQWPqVZ23q83mKylyyFP41xBsnQJLPvKfhwtsDQO1zQ7zEv+kQZq
D35h9E0v4m2GcJtPDtSoR9R2ewKBgQDAqS3vquwC7nS29Ngx1fN7mhoX37dkeMhx
1LpVLlbcco8zfBuDa4cBM0UtgoVan0e9YpKeL7dREMo5ITFBRrMQF93g+Q7WjRwT
tqfHLUBckZTGf4B1GQDDUn5aK07ILBcfEuL+v+aNoy9C8jPJJkEtcat5ruzOCAZa
UlCVRHX4nwKBgEdTWpnYcUXnp6gNoF01RT07M+lvEIJrO5wsj2cxYVb6m+eRsOhj
0kle/kuTmEPvlIkfpX5G6Fd8+zdH8HLc2R2cQNIM6K0JBXvY6qVxxRDFNfe+kvSY
eZ7xuUrb+GUh2xelxk8WVZeg6AqIh+KOH/YW11nx3sXKKGUc655E81tnAoGAYwxX
Nnk8HwGy9YCJSY3CQNBoC9ATO88w1fzU0wgg1fL7li9/AaCdZsuSDCSnJIDw4/ey
gyrq5v1nydk7tmB/nI14n7nLnBgt0CC+vxKPnUenIinYw9rX3pMhrH/JX/Xy6SHP
m8LS6Ax2NsfIQeit54wh6Uw6KG5Nvc/F6AerUucCgYBwo+/d40cIsAfLkcJtX8D1
G3HTvKjCY/cxnaUjVIoCv6aeOTXpKEpURfH7O4LlfNuqkZ6zAgSFI5udQZ1NIeBS
7eaYcep5kYDvvf8v9iL/ZkvTe53MwcrEhxWFMb1++R5hHwAiWhIEAuNb3XzICuZk
PQkpVdZJjyS5VWjmRa6s2Q==
-----END PRIVATE KEY-----
'''
pub_key_generated = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAleIvXIwELVJCAHJwUbOt
iFYBtMdbKj4tPbnB8Q29V05NhWWAs+AwY3N9W2QwLczWdDNlxsQcc3y1kIPLynCM
BbqYctD+4flihM+H8k2QHgWn0nKHmxSL77zC2/TIAItSqkch0vC55WEMdLDpU7d0
+V+T/NC1DUeUhaxsxUspKoYr6vtF3IbxcIugIx6tNKwYr/T+RPhBEi8GZ8Jd50aO
+aWATAWQwi2NMzoPbX6z4Wonp7ZXOVjz49FP9O1PNIQrWO/Z1s2CJqFAAhMswBH5
M/n0ZmFB+gDcSShaUIdeW4HXi3dfSr3V0hc3d5tHjzNsOBQLrvZ4JkvBS8NEQfO+
ZQIDAQAB
-----END PUBLIC KEY-----'''

# don't really know how to prove that I was able to sign something
# I signed the public key file with the private key and got a Verified OK

#Include a short README explaining your code's functionality
#works