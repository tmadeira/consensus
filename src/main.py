import simulation

for n in [3, 5, 7, 11, 17]:
    for tp in ['cycle', 'complete']:
        for mem in [[1], [0.8, 0.2], [0.6, 0.3, 0.1]]:
            print(n, tp, mem, simulation.run(n, tp=tp, memory=mem))

