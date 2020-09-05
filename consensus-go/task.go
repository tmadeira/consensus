package main

import (
	"fmt"
	"math/rand"
)

type task_t struct {
	n    int
	p    float64
	seed int
}

func consume(id int, tasks <-chan task_t, done chan<- bool) {
	for t := range tasks {
		run(t)
	}

	done <- true
}

func run(t task_t) {
	r := rand.New(rand.NewSource(int64(t.seed)))

	A := make([]int, t.n)
	B := make([]int, t.n)
	for i := 0; i < t.n; i++ {
		A[i] = r.Intn(2)
		B[i] = A[i]
	}

	count := 0
	for {
		if consensus(A) {
			break
		}

		copy(B, A)

		for i := 0; i < t.n; i++ {
			old := (B[(i+t.n-1)%t.n] >> 1) + (B[(i+1)%t.n] >> 1)
			cur := (B[(i+t.n-1)%t.n] % 2) + (B[(i+1)%t.n] % 2)

			rnd := r.Float64()
			A[i] = A[i] << 1
			if 2.0*rnd < float64(old)*(1-t.p)+float64(cur)*t.p {
				A[i] |= 1
			}
			A[i] %= 4
		}

		count += 1
	}

	fmt.Printf("%d\n", count)
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
