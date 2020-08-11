# consensus simulation

## Usage

```py
import simulation

# 3-cycle, no memory.
simulation.run(3)
# n = 3 ; colors = 2 ; init = [0 1 1] ; mem = [1.0]
# tp = cycle ; exp. rounds = 4.094 ± 3.5957146716612534

# 5-path, last state in memory (`tp` defaults to 'cycle').
simulation.run(5, tp='path', memory=[0.8, 0.2])
# n = 5 ; colors = 2 ; init = [0 1 1 0 1] ; mem = [0.8, 0.2]
# tp = path ; exp. rounds = 9.802 ± 8.2841291636478

# K_7, last 2 states in memory.
simulation.run(7, tp='complete', memory=[0.7, 0.2, 0.1])
# n = 7 ; colors = 2 ; init = [0 1 1 0 1 1 1] ; mem = [0.7, 0.2, 0.1]
# tp = complete ; exp. rounds = 10.146 ± 9.751342676780466

# K_5 with 4 colors and no memory (`colors` defaults to 2).
simulation.run(5, tp='complete', colors=4)
# n = 5 ; colors = 4 ; init = [0 3 1 0 3] ; mem = [1.0]
# tp = complete ; exp. rounds = 7.39 ± 5.0455822260666805
```
