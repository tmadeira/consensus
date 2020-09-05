package main

import "math/rand"

func cycle(t task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, B := initial(t.n, r)

	count := 0
	for {
		if consensus(A) {
			break
		}

		copy(B, A)

		for i := 0; i < t.n; i++ {
			A[i] = update(B, r.Float64(), i, []int{(i + t.n - 1) % t.n, (i + 1) % t.n}, t.p)
		}

		count++
	}

	return count
}
