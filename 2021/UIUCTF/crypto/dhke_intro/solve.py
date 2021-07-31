c = bytearray.fromhex("b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6")

'''
g,p ∈ [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ] <- can guess
a ∈ [1,p]
b ∈ [1,p]
k = g^{a*b} (mod p)
'''

gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]


for k in range(30):
    