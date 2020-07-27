from sage.all import *
c=32949
n=64741
e=42667
factors = factor(n)
totient = prod(i[0]-1 for i in factors)
d = inverse_mod(e,totient)
m = pow(c,d,n)
print(m)
#18429
#flag from flag.zip is csictf{gr34t_m1nds_th1nk_4l1ke}
