#include <stdio.h>

int main() {
  int total = 0;
  for (int i = 0; i < 100; i++) {
    for (int j = 0; j < 100; j++) {
      total += i + j;
    }
  }
  printf("Total: %d\n", total);
  return 0;
}
