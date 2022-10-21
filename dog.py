import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.alive = True
    def to_sleep(self):
        self.gladness + 5
    def to_chill(self):
        attck = random.randint(1, 4)
        if attck == 1:
            print("Nice attack")
            self.gladness += 20
        if attck == 2:
            print("we lose")
            self.gladness -= 40
        self.gladness += 5
    def is_alive(self):
        if self.gladness <= 0:
            print("Died...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 2)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = Dog(name= "Nick")

for day in range(10):
    if nick.alive == False:
        break
    nick.live(day)

