package consensus

import "fmt"

func consume(id int, tasks <-chan Task, done chan<- bool) {
	for t := range tasks {
		c := t.Run()
		fmt.Printf("%d\n", c)
	}

	done <- true
}
