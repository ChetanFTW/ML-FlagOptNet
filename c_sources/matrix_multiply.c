// matrix_multiply.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 300

int main() {
    int i, j, k;
    int **a = malloc(SIZE * sizeof(int *));
    int **b = malloc(SIZE * sizeof(int *));
    int **c = malloc(SIZE * sizeof(int *));
    
    for (i = 0; i < SIZE; i++) {
        a[i] = malloc(SIZE * sizeof(int));
        b[i] = malloc(SIZE * sizeof(int));
        c[i] = malloc(SIZE * sizeof(int));
    }
    
    // Initialize matrices
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            a[i][j] = i + j;
            b[i][j] = i - j;
            c[i][j] = 0;
        }
    }
    
    // Measure start time
    clock_t start = clock();
    // Matrix multiplication
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            for (k = 0; k < SIZE; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    
    // Measure end time
    clock_t end = clock();
    double time_taken = ((double)(end - start)) * 1000.0 / CLOCKS_PER_SEC;
    printf("Time taken: %.2f ms\n", time_taken);
    // Cleanup
    for (i = 0; i < SIZE; i++) {
        free(a[i]);
        free(b[i]);
        free(c[i]);
    }
    
    free(a);
    free(b);
    free(c);
    return 0;
}
