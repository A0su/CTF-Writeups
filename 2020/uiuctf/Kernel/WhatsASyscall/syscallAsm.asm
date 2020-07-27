global _start

_start:
	mov eax, 0xe
	mov edi, 0x0
	int 0x80
	ret	

