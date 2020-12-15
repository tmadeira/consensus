The Influence of Memory in Multi-Agent Consensus
==

David Kohan Marzagão, Luciana Basualdo Bonatto, Tiago Madeira, Marcelo Matheus
Gauy, Peter McBurney

This repository contains code, data and plots used in an accepted paper that
will be published in the 35th AAAI Conference on Artificial Intelligence (AAAI
2021).

_Link for the final version of the paper coming soon._

### Usage

To compile:

```
$ make
```

You must have [Go](https://golang.org/). The code was tested with go version
go1.15.1 linux/amd64.

To run:

```
$ ./simulator <tp> <n> <times> <memory> [<threads>] [<seed>]
```

where `<tp>` is the network structure, `<n>` is the number of nodes, `<times>`
is the number of times to run the experiment, `<memory>` is the probability of
looking to current state (i.e., use `1.0` to make an experiment with no
memory), `<threads>` is the number of threads the simulator should use,
`<seed>` is the random seed.

**Supported network structures:**
biclique, bintree, clique, cycle, path, torus.

See exp1.py for an example of how to use the simulator to produce some useful
data. See exp1-plot.py for an example of how to plot data computed by exp1.py.

See plots/ for generated plots.
