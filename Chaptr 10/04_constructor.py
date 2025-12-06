class mtinformation:
    name = "Tanvir"
    language = "python"
    age = "18"
    dream = "gain a well payed job"
    salary = 13000
   

    def __init__(self,name,language,salary): # this is a bunder method
        self.name = name
        self.language = language
        self.salary = salary


    
    def getinfo(self):
        print(f"his age is {self.age} and his dream is {self.dream}")

    @staticmethod
    def get():
        print("Thank you")

tanvir = mtinformation("harry","python",120000)
print(tanvir.name,tanvir.salary,tanvir.language)

tahir = mtinformation()
print(tahir.name)