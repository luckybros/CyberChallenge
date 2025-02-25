from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random

key = bytes.fromhex('f8ac4da18ed4ca86')
iv = Random.new().read(DES.block_size)

plaintext = 'La lunghezza di questa frase non è divisibile per 8'.encode('utf-8')
#Padding_scheme = x923

cipher = DES.new(key, DES.MODE_CBC, iv)
ct = cipher.encrypt(pad(plaintext, DES.block_size, 'x923'))

print("PART 1")
print(ct.hex())
print(iv.hex())




