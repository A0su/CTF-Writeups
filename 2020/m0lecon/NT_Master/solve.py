from pwn import *
'''
a,b (a>b) (a,b > 0)

gcd(a,b) + lcm(a,b) = N

Known: gcd(a,b)*lcm(a,b) = a*b

gcd is the largest common multiple of a and b
lcm is the smallest multiple that a and b share
'''

host = 'challs.m0lecon.it'
port = 10000

r = remote(host,port)
shit = r.recvuntil('N = ')
val = int(r.recv())
r.sendline(str(val-1) + ' ' +  str(1))

for i in range(9):
    text = r.recvuntil('N = ')
    val = int(r.recv())
    r.sendline(str(val-1) + ' ' +  str(1))
print(r.recv())

#flag: ptm{as_dumb_as_a_sanity_check}
