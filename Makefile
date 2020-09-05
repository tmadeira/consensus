simulator:
	cd consensus-go && go build . && mv consensus-go ../simulator

clean:
	rm -rf simulator
