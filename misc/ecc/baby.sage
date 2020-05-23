from Crypto.Util.number import bytes_to_long as btl
from Crypto.Random.random import randint

p = 16467119735301371251
F = GF(p)
a = F(15992)
b = F(1935)
E = EllipticCurve(F, [a, b])
G = E.gens()[0] # generator point
k = randint(int(1), int(p-1)) # private
Q = k*G # public

flag_content = b'REDACTED'
fullflag = b'MISCCTF{' + flag_content + '}'
x = F(btl(flag_content))
rhs = x^3 + a*x + b
K = (p-1)//2
y = pow(rhs, (K+1)//2, p)
assert y^2 == rhs
flag_point = E((x, y)) # flag is the x component

r = randint(int(1), int(p-1))
rG = r*G
S = r*Q
e = flag_point + S

print 'p={}\\na={}\\nb={}\\nQ={}\\nrG={}\\ne={}'.format(p,a,b,Q,rG,e)
