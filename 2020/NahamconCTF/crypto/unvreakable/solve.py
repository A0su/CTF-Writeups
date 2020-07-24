with open('out','rb') as fp:
    c = fp.readline()

def printFlag(s):
    for i in s:
        print(chr(i),end='')

ct = []
for i in c:
    ct.append(i)
ct[0] = ct[0]-104
ct[3] = ct[3] -104

print(ct)
printFlag(ct)


