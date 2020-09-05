package main

import "math/rand"

func path(t task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, B := initial(t.n, r)

	count := 0
	for {
		if consensus(A) {
			break
		}

		copy(B, A)

		for i := 0; i < t.n; i++ {
			e := []int{(i + t.n - 1) % t.n, (i + 1) % t.n}
			if i == 0 {
				e = []int{0, 1}
			} else if i == t.n-1 {
				e = []int{t.n - 2}
			}
			A[i] = update(B, r.Float64(), i, e, t.p)
		}

		count++
	}

	return count
}
