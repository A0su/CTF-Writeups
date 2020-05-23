from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd
from secrets import flag

n1, n2, n3 = getPrime(1024)*getPrime(1024), getPrime(1024)*getPrime(1024), getPrime(1024)*getPrime(1024)
assert(gcd(n1, n2) == gcd(n1, n3) == gcd(n2, n3) == 1)
e = 3

m = bytes_to_long(flag)

c1, c2, c3 = pow(m, e, n1), pow(m, e, n2), pow(m, e, n3)

print(f'n1={n1}\nn2={n2}\nn3={n3}\nc1={c1}\nc2={c2}\nc3={c3}')
