#include <stdio.h>

int main() {
  for (int i = 0; i < 5; i++) {
    switch (i) {
      case 0: printf("Zero\n"); break;
      case 1: printf("One\n"); break;
      case 2: printf("Two\n"); break;
      default: printf("Other\n"); break;
    }
  }
  return 0;
}
