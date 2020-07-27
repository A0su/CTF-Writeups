# pwn intended 0x1
Disassembly we can see that there is a jump to a function that will call system('cat flag.txt')
This jump occurs if the the allocated variable var_4h isn't still 0
To corrupt the variable we just overflow the buffer and write just enough to alter the value

csictf{y0u_ov3rfl0w3d_th@t_c0ff33_l1ke_@_buff3r}
