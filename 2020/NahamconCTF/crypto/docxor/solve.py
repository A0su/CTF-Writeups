from string import printable

def isPrintable(s):
    for i in s:
        if i not in printable:
            return False
    return True

def bXOR(s,c):
    res = ''
    for i in s:
        res += chr(ord(i)^c)
    return res

if __name__ == '__main__':
    with open('hw','rb') as fp:
        text = fp.readlines()

    c = []
    #cleaning
    for i in text:
        if i != b'\n':
            c.append(i)
    
    one = c[-1][0:4]
    two = c[-1][4:8]
    three = c[-1][8:12]
    four = c[-1][12:16]


    cont = [one,two,three,four]
    transposed = [[],[],[],[]]
    assert len(one) == len(two)
    assert len(two) == len(three)
    assert len(three) == len(four)

    for i in range(4):
        for j in range(4):
            transposed[i].append(chr(cont[j][i]))

    keys = [[],[],[],[]]
    for block in transposed:
        for char in range(256):
            if isPrintable(bXOR(block,char)):
                keys[transposed.index(block)].append(chr(char))
    print(keys)
