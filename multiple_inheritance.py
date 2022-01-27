class Flyer:
    def fly(self):
        print("flying...")

    def say_hi(self):
        print("Flyer say hi")

class Swimmer:
    def swim(self):
        print("swimming...")

    def say_hi(self):
        print("Swimmer say hi")

class FlyingFish(Swimmer, Flyer):
    pass


flying_fish = FlyingFish()
flying_fish.fly()
flying_fish.swim()
flying_fish.say_hi()