c = [0x83,0xea,0x8d,0xe8,0x85,0xfe,0x93,0xe1,0xbe,0xcd,0xb9,0xd8,0xaa,0xc1,0x9e,0xf7,0xa8,0xce,0xab,0xce,0xa2,0xfd,0x8f,0xfa,0xf9,0x98,0xfd,0x89]

rodata = [0xe4,0x73,0x72,0x63, 0x2f,0x6c,0x69,0x62,0x2e,0x72,0x73,0x00, 0x2f,0xf8,0xff,0xff,0x67,0xf7,0xff,0xff, 0x1f,0xf8,0xff,0xff, 0x67,0xf7,0xff,0xff]

for x,y in zip(c,rodata):
    print(chr(x^y),end='')


