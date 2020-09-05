package main

import "math/rand"

func biclique(t task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, _ := initial(t.n, r)

	count := 0
	for {
		if consensus(A) {
			break
		}

		m := t.n / 2

		S, T := make([]int, 4), make([]int, 4)
		for i := 0; i < m; i++ {
			S[A[i]]++
		}
		for i := m; i < t.n; i++ {
			T[A[i]]++
		}

		for i := 0; i < m; i++ {
			old := T[2] + T[3]
			cur := T[1] + T[3]

			A[i] = (A[i] << 1) % 4
			if float64(t.n-m)*r.Float64() < float64(old)*(1-t.p)+float64(cur)*t.p {
				A[i] |= 1
			}
		}

		// m is in T. But it is a special case because it has a self-loop.
		{
			old := S[2] + S[3] + (A[m] >> 1)
			cur := S[1] + S[3] + (A[m] % 2)

			A[m] = (A[m] << 1) % 4
			if float64(m+1)*r.Float64() < float64(old)*(1-t.p)+float64(cur)*t.p {
				A[m] |= 1
			}
		}

		for i := m + 1; i < t.n; i++ {
			old := S[2] + S[3]
			cur := S[1] + S[3]

			A[i] = (A[i] << 1) % 4
			if float64(m)*r.Float64() < float64(old)*(1-t.p)+float64(cur)*t.p {
				A[i] |= 1
			}
		}

		count++
	}

	return count
}
