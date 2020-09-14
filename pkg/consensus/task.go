package consensus

import (
	"fmt"
	"math/rand"
)

// Task is an experiment to run.
//
// - `tp`: network structure (see Task.Run for a list of options).
// - `n`: number of nodes in the graph.
// - `p`: probability of looking to current state (p_0).
// - `seed`: random seed.
type Task struct {
	tp   string
	n    int
	p    float64
	seed int
}

// Run runs a task and returns the number of rounds it takes to finish.
//
// Accepted structures: biclique, bintree, clique, cycle, path, torus.
func (t Task) Run() int {
	switch t.tp {
	case "biclique":
		return biclique(t)
	case "bintree":
		return bintree(t)
	case "clique":
		return clique(t)
	case "cycle":
		return cycle(t)
	case "path":
		return path(t)
	case "torus":
		return torus(t)
	default:
		panic(fmt.Sprintf("Unknown type '%v'.\n", t.tp))
	}
}

func consensus(a []int) bool {
	if a[0] == 1 || a[0] == 2 {
		return false
	}

	for i := 1; i < len(a); i++ {
		if a[i] != a[0] {
			return false
		}
	}

	return true
}

func initial(n int, r *rand.Rand) ([]int, []int) {
	A, B := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		A[i] = r.Intn(2)
		A[i] = (A[i] << 1) + A[i]
	}

	copy(B, A)
	return A, B
}

func update(A []int, rnd float64, pos int, edges []int, p float64) int {
	old, cur := 0, 0
	for _, e := range edges {
		old += A[e] >> 1
		cur += A[e] % 2
	}

	ret := (A[pos] << 1) % 4
	if float64(len(edges))*rnd < float64(old)*(1-p)+float64(cur)*p {
		ret |= 1
	}
	return ret
}
