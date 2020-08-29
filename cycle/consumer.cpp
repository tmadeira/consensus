#include <stdio.h>
#include <stdlib.h>

#include "consumer.h"
#include "queue.h"
#include "task.h"

void *consume(void *p) {
  consumer_t *C = (consumer_t *) p;

  while (1) {
    task_t t = queue_pop(C->Q);
    if (t.nop) {
      break;
    }

    run_task(t);
  }

  return 0;
}
