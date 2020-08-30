consensus
==

To compile:

```
$ make
```

To run:

```
$ ./simulator <tp> <n> <times> <memory> [<threads>] [<seed>]
```

where `<tp>` is the graph type, `<n>` is the number of nodes, `<times>` is the
number of times to run the experiment, `<memory>` is the probability of looking
to current state (i.e., use `1.0` to make an experiment with no memory),
`<threads>` is the number of threads the simulator should use, `<seed>` is the
random seed.

The most important part of the code is in src/task.cpp.

See fig1.py for an example of how to use the simulator to produce some useful
data. See fig1-plot.py for an example of how to plot data computed by fig1.py.
