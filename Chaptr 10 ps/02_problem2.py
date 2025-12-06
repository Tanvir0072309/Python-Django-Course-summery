class calculator:
    def __init__(self,n):
        self.n = n

    def squre(self):
        print(f"{self.n*self.n}")

    def cube(self):
         print(f"{self.n*self.n*self.n}")

    def squreroot(self):
         print(f"{self.n**1/2}")


a = calculator(4)
a.cube()
a.squre()
a.squreroot()


        