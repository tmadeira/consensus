CXX=g++
CXXFLAGS=-pedantic -Wall -O2 -std=c++11
LIBS=-lpthread

cycle: main.o consumer.o queue.o task.o
	$(CXX) -o $@ $^ $(CXXFLAGS) $(LIBS)

clean:
	rm -rf cycle *.o
