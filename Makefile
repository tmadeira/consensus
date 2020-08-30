CXX=g++
CXXFLAGS=-pedantic -Wall -O3 -std=c++11
LIBS=-lpthread

simulator: src/main.o src/consumer.o src/queue.o src/task.o
	$(CXX) -o $@ $^ $(CXXFLAGS) $(LIBS)

clean:
	rm -rf simulator src/*.o
