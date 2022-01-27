class Animal:
    def __init__(self) -> None:
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eating...")

class Mammal(Animal):
    def __init__(self) -> None: #this constructor overriding de constructor of super class 
        super().__init__() # execute the super class constructor
        print("Mammal constructor")
        self.wight = 2

    def walk(self):
        print("walking...")

class Fish(Animal):
    def swim(self):
        print("swimming...")

m = Mammal()
print(f"Mammal age -> {m.age}")
m.eat()
m.walk()