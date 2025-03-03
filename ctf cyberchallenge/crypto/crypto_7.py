from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = bytes.fromhex('f8ac4da18ed4ca86')
iv = get_random_bytes(DES.block_size)

plaintext = 'La lunghezza di questa frase non è divisibile per 8'.encode('utf-8')
#Padding_scheme = x923

cipher = DES.new(key, DES.MODE_CBC, iv)
ct = cipher.encrypt(pad(plaintext, DES.block_size, 'x923'))

print("PART 1")
print(ct.hex())
print(iv.hex())


"""
Cipher = AES256
Mode of operation = CFB
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
Padding scheme = pkcs7 (block size = 16)
Segment size = 24

"""

plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'.encode('utf-8')
iv = Random.new().read(AES.block_size)
key = get_random_bytes(16)
