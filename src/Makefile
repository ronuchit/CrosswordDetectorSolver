CC = g++
CFLAGS= -g -Wall -I. -I./X11
LDFLAGS= -g -Wall

#Libraries
CCOPTS = -c
LIBRARIES = -L./CImg -lX11 -lpthread

#Final Files and Intermediate .o files
RM = /bin/rm -f
all: main

TARGET = hack
main: ImageProcess.o
	$(CC) $(LDFLAGS) -o $(TARGET) $^  $(LIBRARIES) 
	$(RM) *.out

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) *.o $(TARGET)

delete:
	$(RM) *.out

preprocess: main.o
	$(CC) $(LDFLAGS) -o $(TARGET) $^ $(LIBRARIES)
