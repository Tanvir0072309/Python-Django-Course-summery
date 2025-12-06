class code:
    a=1
    @classmethod
    def mycode(self):
        print(self.a)

class programmer(code):
    b=4
        

o = programmer()
o.a = 45
o.mycode()