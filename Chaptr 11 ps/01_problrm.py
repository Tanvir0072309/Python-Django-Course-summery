class twoDvactor:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def saw(self):
        print(f"this is {self.i} and the j is {self.j}")

class threeDvactor(twoDvactor):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def saw(self):
        print(f"{self.i}i + {self.j}j = {self.k}k")

a = twoDvactor(1,2)
a.saw()
b = threeDvactor(1,2,3)
b.saw()