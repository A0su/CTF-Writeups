we need to write shellcode that allows us to call the syscall `SANDBOX_SPECIAL`

reading through the documentation this kernel uses an i386 ISA so an example program to call this syscall is

```asm
global _start
_start:
	mov eax, 0xe
	mov edi, 0x0
	int 0x80
	ret
```

the procedure of getting the opcodes is as follows:
	1. write the .asm file
	2. assemble using `nasm -f elf32 -o out.o syscallAsm.asm`
	3. link using `ld -m elf_i386 out.o -o out`
	4. get the hex using `objdump -d out`

`flag: uiuctf{5ysc4ll_g4ng_sysc4ll_g4ng}`


