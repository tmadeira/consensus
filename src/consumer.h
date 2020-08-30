#ifndef __CONSUMER_H
#define __CONSUMER_H

#include <pthread.h>

#include "queue.h"

typedef struct {
  int id;
  queue_t *Q;
  pthread_mutex_t *print_mutex;
} consumer_t;

void *consume(void *p);

#endif
