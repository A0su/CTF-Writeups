#include <stdio.h>

#include <stdlib.h>

#define C char
# define CC char ** 
#define SP short * 
#define I int
# define R return
# define U unsigned
# define P printf

void p(char * a, int i) {
    printf("%c", a[i]);
  }

int main(int i, char ** c) {
  char _1[19] = {'_','a','c','d','e','h','i','k','l','m','n','o','p','r','s','u','w','y','\0'};
  if (i < 2) return 1;
  int _2 = atoi(c[1]);
  if (((unsigned char * ) & _2)[0] == 0xAF) {
    if (((short *) & _2)[1] == 0x3174) {
      if (((_2 >> 22) & 0xFF) == 0xC5) {
        if ( * (((char * )(( & _2) + 2)) - 7) == 0x19) {
          if (((((short *)(((char * )( & _2)) + 13) - 5)[0] >> 0) & 0xff) == 0x31) {
            printf("kks{");
            p( _1, 2);
            p(_1, _2 >> 24 & 0xFF00);
            p(_1, ((_2 & 1) << 2) | 2);
            p(_1, (( 2 >> 24) & 0xF) * 10 + ((_2 >> 16) & 0xF));
            p(_1, _2 >> 31);
            p(_1, ((char * ) & _2)[1] - 11);
            p(_1, 6);
            p(_1, (_2 + 10) & 0x0000000f);
            p(_1, 014);
            p(_1, i << 2);
            p(_1, i << 2 >> 1);
            p(_1, 000 * 003);
            p(_1, "P" [0] - 69);
            p(_1, (_2 >> 4) % 16);
            p(_1, 2147483648l >> 28);
            p(_1, ( * (unsigned char * ) & _2) - 0x9e);
            p(_1, 000);
            int n = 2 << 5, m = 5;
            while ((m < 11) && (n >>= 2)) {
              p(_1, n);
              p(_1, m);
              m *= 2;
            }
            p(_1, '_' - '_');
            P("%c", 0x76 + (_2 >> 28));
            p(_1, 10 + ((_2 >> 24) & 0xf));
            p(_1, *(((C * ) & _2) + 3) % 16 + 14);
            p(_1, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 - 45);
            p(_1, (P("%s", "") + 1) % 16), p(_1, 13), p(_1, ((C * )( & _2))[2] % 16), P("_");
            p(_1, 5 - 02);
            p(_1, 0x4 - (-9));
            p(_1, 003 - (-12));
            p(_1, 2 - (-010));
            printf("%c", _1[7]);
            printf("}\n");
            }
          }
        }
      }
    }
    return 0;
  }