import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.alive = True
        self.money = 100
    def to_work(self):
        print("Time to work")
        self.gladness += 3
        self.money += 1000
    def to_chillfriend(self):
        self.gladness += 10
        self.money -= 200
    def to_study(self):
        print("Time to study")
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 5
    def to_chill(self):
        print("time to rest")
        self.gladness += 5
    def casino(self):
        print("i will in casino")
        casinorand = random.randint(1, 2)
        if casinorand == 1:
            print("Блин,больше не прийду - 1000")
            self.money -= 3000
            self.gladness -= 30
        if casinorand == 2:
            print("Вот это жекпот 5000")
            self.money += 5000
            self.gladness += 20
    def is_alive(self):
        if self.money <= 0:
            print("Cash out...")
            print("But i need to work harder (i work this night)")
            self.gladness -= 10
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"money = {round(self.money,2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
            self.to_work()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4:
            self.casino()

nick = Student(name= "Nick")

for day in range(35000):
    if nick.alive == False:
        break
    nick.live(day)
