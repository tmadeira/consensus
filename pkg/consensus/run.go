package consensus

// Run performs an experiment with `tp` network structure (see Task.Run
// for a list of accepted structures), `times` times, using p_0=`p`,
// `threads` threads, and using `seed` as random seed.
func Run(tp string, n, times int, p float64, threads, seed int) {
	tt := make(chan Task)
	done := make(chan bool)

	go produce(tt, tp, n, times, p, seed)

	for i := 0; i < threads; i++ {
		go consume(i, tt, done)
	}

	for i := 0; i < threads; i++ {
		<-done
	}
}
