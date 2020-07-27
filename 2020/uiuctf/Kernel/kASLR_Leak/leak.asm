global _start

_start:
	mov eax, 0xe
	mov edi, eax
	int 0x80
	ret

