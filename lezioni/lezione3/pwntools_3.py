from pwn import *

conn = remote('localhost', 1330)
conn.recvrepeat(0.2)
conn.sendline('whoami')
data = conn.recvline(1)

if b"osboxes" in data:
    log.success("you got the root shell")
    conn.interactive()
    