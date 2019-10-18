# General Skills

# 2Warm - 50
Can you convert the number 42 (base 10) to binary (base 2)?
 `python -c 'print(bin(42))'`  gives us 0b101010
</br>Flag: picoCTF{101010}


# Lets Warm Up - 50
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

 `python -c 'print("70".decode("hex"))'`, gives us 'p' 
 </br>Flag: picoCTF{p}

# Warmed Up - 50
What is 0x3D (base 16) in decimal (base 10).

 `python -c 'print(0x3D)'`
 </br> Flag: picoCTF{61}

# Bases
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
```
a0su@a0su:~$ echo 'bDNhcm5fdGgzX3IwcDM1' | base64 -d
l3arn_th3_r0p35
```
# First Grep - 100
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_5_452e1c1630eb14b6753e9a155c3ae588 on the shell server.
```
a0su@a0su:~/Downloads$ grep 'pico' file
picoCTF{grep_is_good_to_find_things_887251c6}
```
# Resources - 100
```
a0su@a0su:~$ curl https://picoctf.com/resources | grep 'picoCTF{'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
																	 100 13164  100 13164    0  <li><code class="highlighter-rouge">picoCTF{r3source_pag3_f1ag}</code> (2019 competition)</li>
																	      <li><code class="highlighter-rouge">picoCTF{xiexie_ni_lai_zheli}</code> (2018 competition)</li>
																				  0   108k      0 --:--:-- --:--:-- --:--:--  108k

```
</br>
Flag: `picoCTF{r3source_pag3_f1ag}`

# strings it - 100
Can you find the flag in file without running it? You can also find the file in /problems/strings-it_3_8386a6aa560aecfba03c0c6a550b5c51 on the shell server.

```
a0su@a0su:~/Downloads$ strings strings | grep 'pico'
picoCTF{5tRIng5_1T_c7fff9e5}
```

# What's a net cat - 100
Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 49816 to get the flag?

```
a0su@a0su:~/Downloads$ nc 2019shell1.picoctf.com 49816 
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_a752a0d3}
```


