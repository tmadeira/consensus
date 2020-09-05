package main

import "fmt"

func consume(id int, tasks <-chan task, done chan<- bool) {
	for t := range tasks {
		var c int
		switch t.tp {
		case "biclique":
			c = biclique(t)
		case "bintree":
			c = bintree(t)
		case "clique":
			c = clique(t)
		case "cycle":
			c = cycle(t)
		case "path":
			c = path(t)
		case "torus":
			c = torus(t)
		default:
			fmt.Printf("Unknown type '%v'.\n", t.tp)
			continue
		}
		fmt.Printf("%d\n", c)
	}

	done <- true
}
