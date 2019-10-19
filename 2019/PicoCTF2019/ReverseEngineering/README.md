# vault-door-training - 50

Given .java file:
```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_e57d01a632a");
    }
}
```

Flag: ```picoCTF{w4rm1ng_Up_w1tH_jAv4_e57d01a632a}```

# vault-door-1 - 100

Given .java file:
```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '7' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '1' &&
               password.charAt(30) == 'f' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'e' &&
               password.charAt(26) == '5' &&
               password.charAt(31) == 'd';
    }
}
```
I used sublime to quickly manipulate the text into a python script that I could sort and get the flag rather than do it manually.

<b>Solution</b>
```python
arr = [(0,'d'),(29,'7'),(4,'r'),(2,'5'),(23,'r'),(3,'c'),(17,'4'),(1,'3'),(7,'b'),(10,'_'),(5,'4'),(9,'3'),(11,'t'),(15,'c'),(8,'l'),(12,'H'),(20,'c'),(14,'_'),(6,'m'),(24,'5'),(18,'r'),(13,'3'),(19,'4'),(21,'T'),(16,'H'),(27,'1'),(30,'f'),(25,'_'),(22,'3'),(28,'e'),(26,'5'),(31,'d')]

s = ''
for i in range(len(arr)):
  s += min(arr)[1]
  arr.pop(arr.index(min(arr)))
print(s)
```
```Flag: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_51e7fd}```

# asm1 - 200
```assembly
What does asm1(0x1b4) return?

asm1:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x421
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x1b4
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0x13
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0x13
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x7f7
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0x13
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0x13
        <+60>:  pop    ebp
        <+61>:  ret  
```
<b>Solution</b>
```C
This one looks simple enough to not attempt to write it into C, but I'll do it anyways

var = 0x1b4 //Same as [ebp+0x8]

//asm1<+0> and asm1<+1> are stack setup


if(var > 0x421){ //false
	if(var != 0x7f7){
		eax = var;
		printf(eax);	
	}
}

if(var != 0x1b4){ //false
	eax = var;
	eax -= 0x13;
	print(eax)
}

eax = var;
eax += 0x13;
print(eax)
```

So the result is 0x1b4 + 0x13 = 0x1c7

```Flag: 0x1c7```

# vault-door-3 - 200

Given .java file:
```java
a0su@a0su:~/Downloads$ cat VaultDoor3.java 
import java.util.*;
class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm16g84c_u_4_m0r846");
    }
}
```

<b>Solution</b>
```
TO DO
```

# asm2 - 250
```assembly
What does asm2(0x10,0x18) return?
asm2:   <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   sub    esp,0x10
        <+6>:   mov    eax,DWORD PTR [ebp+0xc]
        <+9>:   mov    DWORD PTR [ebp-0x4],eax
        <+12>:  mov    eax,DWORD PTR [ebp+0x8]
        <+15>:  mov    DWORD PTR [ebp-0x8],eax
        <+18>:  jmp    0x50c <asm2+31>
        <+20>:  add    DWORD PTR [ebp-0x4],0x1
        <+24>:  add    DWORD PTR [ebp-0x8],0xcb
        <+31>:  cmp    DWORD PTR [ebp-0x8],0xb693
        <+38>:  jle    0x501 <asm2+20>
        <+40>:  mov    eax,DWORD PTR [ebp-0x4]
        <+43>:  leave  
        <+44>:  ret  
```
<b>Solution</b>
```c
var1 = [ebp+0x8] = 0x10
var2 = [ebp+0xc] = 0x18

eax = 0x18
[ebp-0x4] =  eax = 0x18
eax = 0x10
[ebp-0x8] = eax = 0x10

//lines <asm+20> to asm<+38> is a while loop
while([ebp-0x8] <= 0xb693){ 
	[ebp-0x4] += 0x1
	[ebp-0x8] += 0xcb
}

eax = [ebp-0x4]


We need to find how many times 203(0xcb) is needs to be added to 16(0x10) and then add that value to [ebp-0x4], which equals 0x18

We can find this to be 231 times so 0x18 + 231 = 255 = 0xff

Flag: picoCTF{0xff}
```
# asm3 - 300
```assembly
asm3(0xcdc485c1,0xd6bd5e88,0xe4c1548d)

asm3:
        <+0>:     push   ebp
        <+1>:     mov    ebp,esp
        <+3>:     xor    eax,eax
        <+5>:     mov    ah,BYTE PTR [ebp+0x8]
        <+8>:     shl    ax,0x10
        <+12>:    sub    al,BYTE PTR [ebp+0xe]
        <+15>:    add    ah,BYTE PTR [ebp+0xc]
        <+18>:    xor    ax,WORD PTR [ebp+0x10]
        <+22>:    nop
        <+23>:    pop    ebp
        <+24>:    ret    
```

```C
/*
eax is a 32bit register
The lower 16bits is composed of ax
Then the lower 8 of ax is composed of al
The higher 8 of ax is composed of ah
It looks like this:
---------------
      eax     | 
--------------- 
       |  ax  | 
---------------
       |ah| al| 
---------------

Size Directives:
BYTE PTR - 1 bytes
WORD PTR - 2 bytes
DWORD PTR - 4 bytes
*/
```