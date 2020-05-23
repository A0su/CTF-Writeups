with open('missing.txt','r') as fp:
    text = fp.readlines()

lines = [
    'ASDFGHJKL:\"',
    'asdfghjkl;\'',
    'QWERTYUIOP{}',
    'qwertyuiop[]',
    'zxcvbnm,./',
    'ZXCVBNM<>?',
    '1234567890-=',
    '!@#$%^&*()_+'
]

def findLine(phrase):
    idx = 0
    for char in phrase:
        if phrase[idx] != ' ':
            break
        idx += 1

    for line in lines:
        if phrase[idx] == line[idx]:
            return line

def cmpLine(tmp,line):
    for i in range(len(line)):
        if line[i] == ' ':
            return tmp[i]

sol = ''
for line in text:
    print(line)
    tmp =''
    if not line.split():
        sol += ' '
    else:
        tmp = findLine(line)
        sol += cmpLine(tmp,line)
    print(sol)

actual =''
for i in range(len(sol)):
    if(i>0):
        if sol[i-1] == '.' and sol[i+1] == '.':
            actual += sol[i]
print(actual.replace(' ',''))