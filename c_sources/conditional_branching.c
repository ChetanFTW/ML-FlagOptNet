#include <stdio.h>

int classify(int x) {
  if (x < 0) return -1;
  else if (x == 0) return 0;
  else if (x < 10) return 1;
  else return 2;
}

int main() {
  for (int i = -5; i <= 15; i++) {
    printf("classify(%d) = %d\n", i, classify(i));
  }
  return 0;
}

