def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

hex_alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
ciphertext_len = len(ciphertext)/2
list_text = []

key = ""
for x in hex_alphabet:
    key = key + x
    for y in hex_alphabet:
        key = key + y
        list_text.append(xor(bytes.fromhex(ciphertext), bytes.fromhex(key)*25))
        key = key[:-1]
    key = key[:-1]  
    break

for text in list_text:
    print(text)


