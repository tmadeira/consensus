package main

import (
	"fmt"
	"os"
	"runtime"
	"strconv"

	"blind/pkg/consensus"
)

func usage(cmd string) {
	fmt.Printf("Usage: %s <tp> <n> <times> <memory> [<threads>] [<seed>]\n", cmd)
	fmt.Printf("Supported types: biclique, bintree, clique, cycle, path, torus.\n")
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

	consensus.Run(tp, n, times, p, threads, seed)
}
