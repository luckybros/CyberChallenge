from pwn import *

r = remote('software-17.challs.olicyber.it', 13000)
r.sendline(b'c')
list = r.recv()

print('LISTA')
print(list)


#r.sendline(list.sum())

