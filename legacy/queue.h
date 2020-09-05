#ifndef __QUEUE_H
#define __QUEUE_H

#include <pthread.h>

#include "task.h"

typedef struct {
  task_t *tasks;
  int length;
  int start;
  int end;
  pthread_mutex_t mutex;
  pthread_cond_t has_something;
} queue_t;

void queue_init(queue_t *Q, int length);
void queue_destroy(queue_t *Q);
void queue_push(queue_t *Q, task_t task);
task_t queue_pop(queue_t *Q);

#endif
