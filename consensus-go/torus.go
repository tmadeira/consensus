package main

import (
	"fmt"
	"math"
	"math/rand"
)

func torus(t task) int {
	r := rand.New(rand.NewSource(int64(t.seed)))
	A, B := initial(t.n, r)

	x := int(math.Sqrt(float64(t.n)))
	y := x

	if x*y != t.n {
		x = int(math.Sqrt(float64(t.n)))
		y = x + 2

		if x*y != t.n {
			panic(fmt.Sprintf("%d*%d != %d", x, y, t.n))
		}
	}

	count := 0
	for !consensus(A) {
		copy(B, A)

		for i := 0; i < x; i++ {
			for j := 0; j < y; j++ {
				edges := []int{
					i*x + (j+y-1)%y,
					i*x + (j+1)%y,
					((i+x-1)%x)*x + j,
					((i+1)%x)*x + j,
				}
				A[i*x+j] = update(B, r.Float64(), i*j+j, edges, t.p)
			}
		}

		count++
	}

	return count
}
