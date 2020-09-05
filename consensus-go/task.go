package main

import "math/rand"

type task struct {
	tp   string
	n    int
	p    float64
	seed int
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
