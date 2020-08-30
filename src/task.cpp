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

void run_cycle(task_t t) {
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

  free(A);
  free(B);
}

void run_torus(task_t t) {
  int m = sqrt(t.n);
  int i, j;
  double old, current, r;
  int top, right, bottom, left;

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

    for (i = 0; i < m; i++) {
      for (j = 0; j < m; j++) {
        left = i * m + ((j + m - 1) % m);
        right = i * m + ((j + 1) % m);
        top = ((i + m - 1) % m) * m + j;
        bottom = ((i + 1) % m) * m + j;

        old = (B[left] >> 1) + (B[right] >> 1) + (B[top] >> 1) + (B[bottom] >> 1);
        current = (B[left] % 2) + (B[right] % 2) + (B[top] % 2) + (B[bottom] % 2);

        r = real(engine);

        A[i*m+j] = (A[i*m+j] << 1) | (4.0 * r <= old*(1-t.mem) + current*t.mem);
        A[i*m+j] %= 4;
      }
    }

    count++;
  }

  printf("%d\n", count);

  free(A);
  free(B);
}

void run_clique(task_t t) {
  int i;
  double old, current, r;
  int counters[4], k;

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

    counters[0] = counters[1] = counters[2] = counters[3] = 0;
    for (i = 0; i < t.n; i++) {
      counters[A[i]]++;
    }

    for (i = 0; i < t.n; i++) {
      k = A[i];
      counters[k]--;

      old = counters[2] + counters[3];
      current = counters[1] + counters[3];

      r = real(engine);
      A[i] = (A[i] << 1) | ((t.n-1) * r <= old*(1-t.mem) + current*t.mem);
      A[i] %= 4;

      counters[k]++;
    }

    count++;
  }

  printf("%d\n", count);

  free(A);
  free(B);
}

void run_task(task_t t) {
  switch (t.tp) {
  case CYCLE:
    run_cycle(t);
    break;
  case TORUS:
    run_torus(t);
    break;
  case CLIQUE:
    run_clique(t);
    break;
  default:
    printf("Skipping task with unknown type.\n");
  }
}
