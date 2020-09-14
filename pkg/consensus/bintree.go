package consensus

import "math/rand"

func bintree(t Task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, B := initial(t.n, r)

	if t.n&(t.n+1) != 0 {
		panic("n+1 must be a power of two")
	}

	count := 0
	for !consensus(A) {
		copy(B, A)

		for i := 0; i < t.n; i++ {
			var e []int

			if i > 0 {
				// Node parent.
				e = append(e, (i-1)/2)
			} else {
				// Root node has self-loop.
				e = append(e, 0)
			}

			if 2*(i+1) < t.n {
				// Node children.
				e = append(e, 2*(i+1)-1, 2*(i+1))
			}

			A[i] = update(B, r.Float64(), i, e, t.p)
		}

		count++
	}

	return count
}
