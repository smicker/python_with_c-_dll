TARGET=simpleMath.so

CPPFLAGS=-Wall -Wextra -O -ansi -pedantic
LDFLAGS=-shared

.PHONY: all clean

all: $(TARGET)

$(TARGET): 
	gcc $(CPPFLAGS) $(OBJECTS) $(LDFLAGS) simpleMath.cpp -o $(TARGET)

clean:
	rm -f $(OBJECTS) $(TARGET)