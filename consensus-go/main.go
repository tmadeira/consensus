package main

import (
	"fmt"
	"os"
	"runtime"
	"strconv"
)

func produce(tt chan<- task, tp string, n, times int, p float64, seed int) {
	for i := 0; i < times; i++ {
		tt <- task{
			tp:   tp,
			n:    n,
			p:    p,
			seed: seed + i,
		}
	}
	close(tt)
}

func usage(cmd string) {
	fmt.Printf("Usage: %s <tp> <n> <times> <memory> [<threads>] [<seed>]\n", cmd)
	os.Exit(1)
}

func main() {
	if len(os.Args) < 5 {
		usage(os.Args[0])
	}

	tp := os.Args[1]

	n, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println(err)
		usage(os.Args[0])
	}

	times, err := strconv.Atoi(os.Args[3])
	if err != nil {
		fmt.Println(err)
		usage(os.Args[0])
	}

	p, err := strconv.ParseFloat(os.Args[4], 64)
	if err != nil {
		fmt.Println(err)
		usage(os.Args[0])
	}

	threads := runtime.NumCPU()
	if len(os.Args) > 5 {
		var err error
		threads, err = strconv.Atoi(os.Args[5])
		if err != nil {
			fmt.Println(err)
			usage(os.Args[0])
		}
	}

	seed := 0
	if len(os.Args) > 6 {
		var err error
		seed, err = strconv.Atoi(os.Args[6])
		if err != nil {
			fmt.Println(err)
			usage(os.Args[0])
		}
	}

	tt := make(chan task)
	done := make(chan bool)

	go produce(tt, tp, n, times, p, seed)

	for i := 0; i < threads; i++ {
		go consume(i, tt, done)
	}

	for i := 0; i < threads; i++ {
		<-done
	}
}
