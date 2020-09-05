package main

import "math/rand"

func clique(t task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, _ := initial(t.n, r)

	count := 0
	for {
		if consensus(A) {
			break
		}

		counters := make([]int, 4)
		for _, a := range A {
			counters[a]++
		}

		for i := 0; i < t.n; i++ {
			k := A[i]
			counters[k]--

			old := counters[2] + counters[3]
			cur := counters[1] + counters[3]

			A[i] = (A[i] << 1) % 4
			if float64(t.n-1)*r.Float64() < float64(old)*(1-t.p)+float64(cur)*t.p {
				A[i] |= 1
			}

			counters[k]++
		}

		count++
	}

	return count
}
