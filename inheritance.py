class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eating...")

class Mammal(Animal):
    def walk(self):
        print("walking...")

class Fish(Animal):
    def swim(self):
        print("swimming...")

m = Mammal()
print(f"Mammal age -> {m.age}")
m.eat()
m.walk()

f = Fish()
print(f"Fish age -> {f.age}")
f.eat()
f.swim()