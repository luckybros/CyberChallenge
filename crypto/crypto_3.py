from base64 import b64decode

string_1 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
string_1_decoded = b64decode(string_1)

string_2 = 664813035583918006462745898431981286737635929725
string_2_encoded =  (string_2).to_bytes(20, "big")

result = string_1_decoded + string_2_encoded
print(result)