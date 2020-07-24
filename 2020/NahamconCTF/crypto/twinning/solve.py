from Crypto.Util.number import inverse

n = 2867698391183
e = 65537
d = inverse(e,tot)
c = 714922572030
#sage factor
p = 1693427
q = 1693429

tot = (p-1)*(q-1)
pin = pow(c,d,n)
#submit pin over nc
#flag{thats_the_twinning_pin_to_win}
