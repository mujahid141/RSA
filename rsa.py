#external Liberaries
import numpy as np
import random
import math
#global variables
p = 17
q = 23

n = p*q 
phiN = (p-1)*(q-1)

print("n:",n,"phin:",phiN)
 

e=0
#encryption 
for i in range(2,phiN):
    if(np.gcd(i,phiN)==1):
        e=i

e = random.randrange(1, phiN)
while math.gcd(e, phiN) != 1:
    e = random.randrange(1, phiN)

print(e)
d = pow(e,-1,phiN)
print(d)

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

publickey = e,n

prinvatkey = d,n

encrypted_text = encrypt(publickey,"Hello")
print("Encryption ", encrypted_text)
decrypted_text = decrypt(prinvatkey,encrypted_text)
print("Decyprtion ", decrypted_text)
