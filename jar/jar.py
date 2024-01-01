import sys
class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError("capacity is not correct!")
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if self.size+n > self.capacity:
            raise ValueError("size can not be greater than capasity")
        else:
            self.size+=n
            return self.size

    def withdraw(self, n):
        if self.size < n :
            raise ValueError("size can not be less withdraw")
        self.size-=n
        return self.size

    @property
    def capacity(self):
         return self._capasity

    @capacity.setter
    def capacity(self,capasity):
        if capasity <0:
            raise ValueError("capasity error")
        self._capasity=capasity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if size <0:
            self._saize = 0
        self._size=size

def main():
    j=Jar()
    j.deposit(10)
    j.withdraw(5)
    print(j.size)
    print(j)
if __name__ == "__main__":
    main()