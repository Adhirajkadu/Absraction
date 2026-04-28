from abc import ABC,abstractmethod
class Abs(ABC):
    def print(self, x):
        print("Passed Value : ",x)

    @abstractmethod
    def task(self):
        print("You are inside abs task ")
class test(Abs):
    def task(self):
        print("You are inside test class")

t = test()
t.task()
t.print(100)