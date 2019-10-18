# General Skills

# 2Warm - 50
Can you convert the number 42 (base 10) to binary (base 2)?
 `python -c 'print(bin(42))'`  gives us 0b101010
<\br>Flag: picoCTF{101010}


# Lets Warm Up - 50
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

 `python -c 'print("70".decode("hex"))'`, gives us 'p' 
 <\br>Flag: picoCTF{p}

# Warmed Up - 50
What is 0x3D (base 16) in decimal (base 10).

 `python -c 'print(0x3D)'`
 <\br> Flag: picoCTF{61}

# Bases
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
```
a0su@a0su:~$ echo 'bDNhcm5fdGgzX3IwcDM1' | base64 -d
l3arn_th3_r0p35
```

