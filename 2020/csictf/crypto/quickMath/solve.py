from sage.all import *
n1 = 86812553978993 
n2 = 81744303091421 
n3 = 83695120256591 
c1 = 8875674977048 
c2 = 70744354709710 
c3 = 29146719498409
e = 3

mod = [n1,n2,n3]
c = [c1,c2,c3]

print(bytes.fromhex(str(CRT(c,mod).nth_root(3))))
#b'h45t4d'
