#include <stdio.h>

int factorial(int n) {
  if (n == 0) return 1;
  return n * factorial(n - 1);
}
int main() {
  for (int i = 0; i < 10; i++) {
    printf("fact(%d) = %d\n", i, factorial(i));
  }
  
  return 0;
}
