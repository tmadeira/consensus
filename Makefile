simulator: cmd/*
	cd cmd/simulator && go build -o ../../simulator .

clean:
	rm -rf simulator
