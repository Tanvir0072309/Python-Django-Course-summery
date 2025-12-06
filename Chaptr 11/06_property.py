class code:
    a=1
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o = code()
o.name = "Tanvir khan"
print(o.name)