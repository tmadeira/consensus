#ifndef __TASK_H
#define __TASK_H

#define CYCLE 0
#define TORUS 1
#define CLIQUE 2
#define PATH 3

typedef struct {
  int tp;
  int n;
  unsigned seed;
  double mem;
  bool nop;
} task_t;

void run_task(task_t task);

#endif
