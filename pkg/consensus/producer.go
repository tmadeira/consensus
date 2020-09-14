package consensus

func produce(tt chan<- Task, tp string, n, times int, p float64, seed int) {
	for i := 0; i < times; i++ {
		tt <- Task{
			tp:   tp,
			n:    n,
			p:    p,
			seed: seed + i,
		}
	}
	close(tt)
}
