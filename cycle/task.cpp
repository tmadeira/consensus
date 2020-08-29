#include <algorithm>
#include <bit>
#include <functional>
#include <random>
#include <stdio.h>

#include "task.h"

using namespace std;

// Test consensus.
bool consensus(int *A, int n) {
  int first = A[0];
  if (first >> 1 != first % 2) {
    return false;
  }

  for (int i = 1; i < n; i++) {
    if (A[i] != first) {
      return false;
    }
  }

  return true;
}

void run_task(task_t t) {
  int i;
  double old, current, r;

  default_random_engine engine(t.seed);
  uniform_int_distribution<int> boolean(0, 1);
  uniform_real_distribution<double> real(0.0, 1.0);

  int *A = (int *) malloc(sizeof(int) * t.n);
  int *B = (int *) malloc(sizeof(int) * t.n);

  // Generate random initial array.
  generate(A, A+t.n, bind(boolean, engine));

  // Fill memory with same initial value.
  for (i = 0; i < t.n; i++) {
    A[i] = (A[i] << 1) + A[i];
  }

  int count = 0;
  while (1) {
    if (consensus(A, t.n)) {
      break;
    }

    copy(A, A+t.n, B);

    old = ((B[t.n-1] >> 1) + (B[1] >> 1)) * (1 - t.mem);
    current = ((B[t.n-1] % 2) + (B[1] % 2)) * t.mem;
    r = real(engine);
    A[0] = (A[0] << 1) | (2.0 * r <= old+current);
    A[0] %= 4;

    for (i = 1; i < t.n-1; i++) {
      old = ((B[i-1] >> 1) + (B[i+1] >> 1)) * (1 - t.mem);
      current = ((B[i-1] % 2) + (B[i+1] % 2)) * t.mem;
      r = real(engine);
      A[i] = (A[i] << 1) | (2.0 * r <= old+current);
      A[i] %= 4;
    }

    old = ((B[t.n-2] >> 1) + (B[0] >> 1)) * (1 - t.mem);
    current = ((B[t.n-2] % 2) + (B[0] % 2)) * t.mem;
    r = real(engine);
    A[t.n-1] = (A[t.n-1] << 1) | (2.0 * r <= old+current);
    A[t.n-1] %= 4;

    count++;
  }

  printf("%d\n", count);
}
