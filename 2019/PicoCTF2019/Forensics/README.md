# like1000 - 250
This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

Rather than running tar 1000 times I wrote a small bash script to repeat it for me.
```bash
for ((i=1000;i>0;i--)); do tar xvf $i.tar; done
```
Flag: ```picoCTF{l0t5_0f_TAR5}```

