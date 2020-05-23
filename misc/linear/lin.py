from secret import flag

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV{}_0123456789?'
ctoi = {k: v for v, k in enumerate(alph)}
n = 4
k = 'gybdnqkjHPvfR9tr'
K = [[ctoi[c] for c in k[i:i+n]] for i in range(0, len(k), n)]

def enc(m):
    if len(m) % n != 0:
        pl = n - len(m) % n
        m += 'a'*pl
    M = [[0 for _ in range(len(m)//n)] for _ in range(n)]
    for r in range(len(M)):
        for c in range(len(M[0])):
            M[r][c] = ctoi[m[c*n + r]]
    R = [[0 for _ in range(len(M[0]))] for _ in range(len(K))]
    for i in range(len(K)):
        for j in range(len(M[0])):
            for k in range(len(K[0])):
                R[i][j] += K[i][k]*M[k][j]
    r = ''
    for i in range(len(R)):
        for j in range(len(R[0])):
            R[i][j] = R[i][j] % 62
            r += str(R[i][j]).rjust(2, '0')
    return hex(int(r))

encrypted_flag = enc(flag)


c = '0x1944cccfb862a01424b14103b06e3ae90f586cb4ca128ba4f0b50c9a6b673e1bd745af2ec53e25e181536c1'