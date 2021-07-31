from gmpy2 import mpz, to_binary

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

with open('flag_enc','rb') as fp:
    c = fp.read()

