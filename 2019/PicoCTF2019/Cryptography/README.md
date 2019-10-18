# The Numbers - 50
The numbers... what do they mean?

Too lazy to upload image, it has the following text:
```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 15}
```
You can notice they changed the letters to a numerical value representative of their positioning in the alphabet.
</br>
The following python program can solve this:
```
arr = ['16','9','3','15','3','20','6','20','8','5','14','21','13','2','5','18','19','13','1','19','15','15']
s = ''
for i in range(len(arr)):
	s+= chr(int(arr[i]) + 64)

print(s)
```
Flag: `PICOCTF{THENUMBERSMASOO}`

# 13 - 100
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}. Just plug into rot13.com.

```
Flag: picoCTF{not_too_bad_of_a_problem}
```

# Easy1 - 100
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

This is a Vignere Ciper. Plug into cryptii.com to solve.

```
Flag: picoCTF{CRYPTOISFUN}
```

# caesar - 100
Ciphertext: ```picoCTF{jyvzzpunaolybipjvunfzpthre}```

As the name suggests this is a caesar cipher. To solve I used rot13.com again and found ROT19 to be the appropriate shift to decode.

```
Flag: picoCTF{crossingtherubicongysimakx}
```

# Flags - 200
TODO - Need to find link again.

#miniRSA - 300
Lets decrypt this: ciphertext? Something seems a bit small

Given: 
```
N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872649611751702430439402967052009248250289961880642561508086676942304787433622315744241706664042782734376502484888131147533970136649038736862434581066144482993850305122145625013872515429 
```

Notice e, the public key, is 3 with this we can take the cube root of cipertext. The only constraint to ensure this works is that the cube root of N is greater than the cube of the ciphertext, which it is in this case.

<b>Solution</b>
```
from gmpy import * 

N =  29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3

c =  2205316413931134031074603746928247799030155221252519872649611751702430439402967052009248250289961880642561508086676942304787433622315744241706664042782734376502484888131147533970136649038736862434581066144482993850305122145625013872515429

print(hex(mpz(root(c,e)[0])).strip('0x').strip('L').decode('hex')) 
```

```
Flag: picoCTF{n33d_a_lArg3r_e_21d2334d}
```

# b00tl3gRSA2 - 400
TODO - hopefully find solution script