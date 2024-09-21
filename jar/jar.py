class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if  (self.size + n) > self.capacity:
             raise ValueError("Jar too small")
        self.size = self.size + n

    def withdraw(self, n):
        if (self.size < n):
            raise ValueError("Not enough cookie")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if self.capacity < size:
            raise ValueError("Size error")
        self._size = size

def main():
    jar=Jar()
    print(jar)
    jar.deposit(12)
    print(jar)
    jar.withdraw(2)
    print(jar)
    print(jar.capacity)

if __name__ == "__main__":
    main()
