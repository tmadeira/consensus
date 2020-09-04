#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "consumer.h"
#include "queue.h"
#include "task.h"

void fail(const char *msg) {
  fprintf(stderr, "%s\n", msg);
  exit(1);
}

void run(int tp, int n, int times, double mem, int num_threads, unsigned seed) {
  // Allocate threads.
  pthread_t *threads;
  threads = (pthread_t *) malloc(sizeof(pthread_t) * num_threads);
  if (!threads) {
    fail("could not allocate threads");
  }

  // Create task queue.
  queue_t Q;
  queue_init(&Q, times + num_threads + 1);

  // Allocate consumers.
  consumer_t *consumers;
  consumers = (consumer_t *) malloc(sizeof(consumer_t) * num_threads);
  if (!consumers) {
    fail("could not allocate consumers");
  }

  // Initialize consumers and start threads.
  for (int i = 0; i < num_threads; i++) {
    consumers[i].id = i;
    consumers[i].Q = &Q;
    pthread_create(&threads[i], NULL, consume, (void *) &consumers[i]);
  }

  // Produce tasks.
  for (int i = 0; i < times; i++) {
    task_t t;
    t.tp = tp;
    t.n = n;
    t.seed = seed+i+1;
    t.mem = mem;
    t.nop = false;
    queue_push(&Q, t);
  }

  // Add nop tasks to the end of the queue.
  for (int i = 0; i < num_threads; i++) {
    task_t t;
    t.nop = true;
    queue_push(&Q, t);
  }

  // Finish threads.
  for (int i = 0; i < num_threads; i++) {
    pthread_join(threads[i], NULL);
  }

  // Free everything.
  queue_destroy(&Q);
  free(threads);
  free(consumers);
}

void usage(const char *cmd) {
  fprintf(stderr, "Usage: %s <tp> <n> <times> <memory> [<threads>] [<seed>]\n", cmd);
  fprintf(stderr, "<tp> options: cycle, torus, clique\n");
  exit(1);
}

int main(int argc, char *argv[]) {
  if (argc < 5) {
    usage(argv[0]);
  }

  int tp = -1;
  if (!strcmp("cycle", argv[1])) {
    tp = CYCLE;
  } else if (!strcmp("torus", argv[1])) {
    tp = TORUS;
  } else if (!strcmp("clique", argv[1])) {
    tp = CLIQUE;
  } else {
    usage(argv[0]);
  }

  int n = atoi(argv[2]);
  int times = atoi(argv[3]);
  double mem = atof(argv[4]);

  int threads = 1;
  if (argc > 5) {
    threads = atoi(argv[5]);
  }

  unsigned seed = 0;
  if (argc > 6) {
    seed = (unsigned) atoi(argv[6]);
  }

  run(tp, n, times, mem, threads, seed);
  return 0;
}
