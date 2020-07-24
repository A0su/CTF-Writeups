from Crypto.Cipher import DES
with open('c.txt','rb') as fp:
    c = fp.readlines()[0]

iv = b'13371337'
c = c[0:len(c)-1]

'''
blocks = []
for i in range(len(c)//8):
    blocks.append(c[i*8:i*8+8])

encIV = bytearray()
#odd blocks

for x,y in zip(p0,blocks[0]):
    encIV.append(x^y)

for num in range(len(blocks)):
    if num%2 == 1:
        for x,y in zip(blocks[num],iv):
            print(chr(x^y),end='')
    print('')
'''

'''Found from:
https://github.com/Alpackers/CTF-Writeups/tree/master/2016/BostonKeyParty/Crypto/des-ofb
'''
keys= [b"\x00\x00\x00\x00\x00\x00\x00\x00"[0:8],b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"[0:8],b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"[0:8],b"\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F"[0:8]]

a = DES.new(keys[0], DES.MODE_OFB, iv)
plaintext = a.decrypt(c)
print(plaintext)

a = DES.new(keys[1], DES.MODE_OFB, iv)
plaintext = a.decrypt(c)
print(plaintext)

a = DES.new(keys[2], DES.MODE_OFB, iv)
plaintext = a.decrypt(c)
print(plaintext)

a = DES.new(keys[3], DES.MODE_OFB, iv)
plaintext = a.decrypt(c)
print(plaintext)
