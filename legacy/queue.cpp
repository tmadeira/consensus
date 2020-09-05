#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "queue.h"
#include "task.h"

void queue_init(queue_t *Q, int length) {
  pthread_mutex_init(&Q->mutex, NULL);
  pthread_cond_init(&Q->has_something, NULL);

  Q->tasks = (task_t *) malloc(sizeof(task_t) * length);
  if (!Q->tasks) {
    fprintf(stderr, "could not allocate queue\n");
    exit(1);
  }

  Q->start = Q->end = 0;
  Q->length = length;
}

void queue_destroy(queue_t *Q) {
  pthread_cond_destroy(&Q->has_something);
  pthread_mutex_destroy(&Q->mutex);
}

void queue_push(queue_t *Q, task_t task) {
  pthread_mutex_lock(&Q->mutex);
  Q->tasks[Q->end++] = task;
  Q->end %= Q->length;
  pthread_cond_signal(&Q->has_something);
  pthread_mutex_unlock(&Q->mutex);
}

task_t queue_pop(queue_t *Q) {
  pthread_mutex_lock(&Q->mutex);
  while (Q->start == Q->end) {
    pthread_cond_wait(&Q->has_something, &Q->mutex);
  }

  task_t task = Q->tasks[Q->start++];
  Q->start %= Q->length;
  pthread_mutex_unlock(&Q->mutex);

  return task;
}
