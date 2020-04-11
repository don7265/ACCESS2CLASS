class car:
    def __init__(self):
        self.brand = "toyota"
        self.model = "corola"
        self.speed = 60
    def display(self):
        print("car details ", self.brand , self.model, self.speed)

class increase :
    def test(inc):
        inc.speed = inc.speed + 10
        inc.display()
c1 = car()
increase.test(c1)
