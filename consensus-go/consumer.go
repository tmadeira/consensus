package main

import "fmt"

func consume(id int, tasks <-chan task, done chan<- bool) {
	for t := range tasks {
		var c int
		switch t.tp {
		case "clique":
			c = clique(t)
		case "cycle":
			c = cycle(t)
		case "path":
			c = path(t)
		default:
			fmt.Printf("Unknown type '%v'.\n", t.tp)
			continue
		}
		fmt.Printf("%d\n", c)
	}

	done <- true
}
