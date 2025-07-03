#include <stdio.h>

int main() {
  int arr[1000];
  for (int i = 0; i < 1000; i++)
    arr[i] = i;

  long sum = 0;
  for (int i = 0; i < 1000; i++)
    sum += arr[i];

  printf("Sum: %ld\n", sum);
  return 0;
}

