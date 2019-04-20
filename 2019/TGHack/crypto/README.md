# American Standrad Code for Information Interchange
Given a decimal number

`84 71 49 57 123 65 83 67 73 73 95 97 110 100 95 121 111 117 95 115 104 97 108 108 95 114 101 99 101 105 118 101 125`

Converting to ASCII gives us:

Flag: `T G 1 9 { A S C I I _ a n d _ y o u _ s h a l l _ r e c e i v e }`

*Remove the Spaces*

Flag: `TG19{ASCII_and_you_shall_receive}`

# Land of Encoding
Given a base64 number

`VEcxOXtiZV9jYXJlZnVsX3doZW5fZHJvcHBpbmdfdGhlX2Jhc2V9`

Decoding this gives us

Flag: `TG19{be_careful_when_dropping_the_base}`

# Rotarius
Given this encrypted message `OB19{ocz_hjno_wvndx_otkz_ja_zixmtkodji}`

Notice that O -> T is a difference of 5, so using ROT-5 we obtain:

Flag: `TG19{the_most_basic_type_of_encryption}`

# Exclusive Magic Club
Given this binary

`00111001 00101000 01000101 01010001 00011110 00010000 00110000 00011100
00110001 00001011 00011000 00000100 00110001 00111101 00010001 00011100
00101011 00011001 00000111 00010001 00110111 00100100 00111011 00000000
00000100 00011000 00001010 00000101 00011111 00110000 00010000 00000001
00000000 00001001`

and what I presume to be a key

`mother_knows_best`

Running it through an XOR cipher

Flag: `TG19{bow_down_to_the_AI_overlords}`

