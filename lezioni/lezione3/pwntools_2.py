from pwn import *

p = process('/bin/sh')
p.sendline('sleep 3; echo hello world;')
