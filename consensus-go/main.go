package main

import (
	"fmt"
	"os"
	"runtime"
	"strconv"
)

func produce(tasks chan<- task_t, n, times int, p float64) {
	for i := 0; i < times; i++ {
		tasks <- task_t{
			n:    n,
			p:    p,
			seed: i,
		}
	}
	close(tasks)
}

func main() {
	if len(os.Args) != 4 {
		fmt.Printf("Usage: %s <n> <times> <p>\n", os.Args[0])
		return
	}

	n, _ := strconv.Atoi(os.Args[1])
	times, _ := strconv.Atoi(os.Args[2])
	p, _ := strconv.ParseFloat(os.Args[3], 64)

	tasks := make(chan task_t)
	done := make(chan bool)

	go produce(tasks, n, times, p)

	threads := runtime.NumCPU()
	for i := 0; i < threads; i++ {
		go consume(i, tasks, done)
	}

	for i := 0; i < threads; i++ {
		<-done
	}
}
