from Crypto.Util.number import inverse
N = 3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091
e = 65537
c = 87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983


assert N%2 == 1 #can try fermat factorization if difference is small

#found in sage
p = 1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428207
q = 1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428213

print(f'difference of factors: {q-p}')

tot = (p-1)*(q-1)
d = inverse(e,tot)
m = hex(pow(c,d,N))[2:]

print(bytearray.fromhex(m))
