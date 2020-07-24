import enchant
from pwn import *
d=enchant.Dict("en_US")


HOST = 'jh2i.com'
PORT = 50012

r = remote(HOST,PORT)
garb = r.recvuntil('\n')

first = r.recv().decode().split(' ')
first = [i.replace('\n','').replace('>','') for i in first]
count = 0
for word in first:
    if(word):
        if d.check(word) == False:
            count += 1
r.sendline(str(count).encode())
garb = r.recvuntil('\n')
garb2 = r.recvuntil('\n')

second = r.recv().decode().split(' ')
second = [i.replace('\n','').replace('>','') for i in second]

notWords = []
for word in second:
    if(word):
        if d.check(word) == False:
            notWords.append(word)

payload = ''
for i in notWords:
    payload += (i+' ')

r.sendline(payload.encode())

garb = r.recvuntil('\n')
garb = r.recvuntil('\n')

third =r.recv().decode().split(' ')
third = [i.replace('\n','').replace('>','') for i in third]

notWords = []
for word in third:
    if(word):
        if d.check(word) == False:
            notWords.append(word)

notWords.sort()
payload = ''
for i in notWords:
    payload += (i+' ')

r.sendline(payload.encode())
garb = r.recvuntil('\n')
garb = r.recvuntil('\n')

four =r.recv().decode().split(' ')
four = [i.replace('\n','').replace('>','') for i in four]
count = 0
for word in four:
    if(word):
        if d.check(word) == True:
            count += 1

r.sendline(str(count).encode())

garb = r.recvuntil('\n')
garb = r.recvuntil('\n')
five =r.recv().decode().split(' ')
five = [i.replace('\n','').replace('>','') for i in five]
words = []
for word in five:
    if(word):
        if d.check(word) == True:
            words.append(word)
payload = ''
for i in words:
    payload += (i+' ')

r.sendline(payload.encode())

garb = r.recvuntil('\n')
garb = r.recvuntil('\n')
five =r.recv().decode().split(' ')
five = [i.replace('\n','').replace('>','') for i in five]
words = []
for word in five:
    if(word):
        if d.check(word) == True:
            words.append(word)
words.sort()
payload = ''
for i in words:
    payload += (i+' ')

r.sendline(payload.encode())

first = r.recv().decode().split(' ')
first = [i.replace('\n','').replace('>','') for i in first]
count = 0
for word in first:
    if(word):
        if d.check(word) == False:
            count += 1
r.sendline(str(count).encode())
r.interactive()



