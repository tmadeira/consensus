package consensus

import "math/rand"

func path(t Task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, B := initial(t.n, r)

	count := 0
	for !consensus(A) {
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
