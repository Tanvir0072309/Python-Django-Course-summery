class mtinformation:
    language = "python"
    age = "18"
    dream = "gain a well payed job"
   
    def getinfo(self):
        print(f"his age is {self.age} and his dream is {self.dream}")

    @staticmethod
    def get():
        print("Thank you")

tanvir = mtinformation()
tanvir.get()

tanvir.getinfo()