
from math import gcd 
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

'''
a,b (a>b) (a,b > 0)

gcd(a,b) + lcm(a,b) = N

Known: gcd(a,b)*lcm(a,b) = a*b

gcd is the largest common multiple of a and b
lcm is the smallest multiple that a and b share
'''
