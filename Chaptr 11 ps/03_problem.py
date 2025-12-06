class Employee:
    salary = 234
    increement = 20
    @property
    def salaryafterincrement(self):
        return (self.salary+self.salary*(self.increement/100))

    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increement = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryafterincrement)
print(e.increement)