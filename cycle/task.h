#ifndef __TASK_H
#define __TASK_H

typedef struct {
  int n;
  unsigned seed;
  double mem;
  bool nop;
} task_t;

void run_task(task_t task);

#endif
