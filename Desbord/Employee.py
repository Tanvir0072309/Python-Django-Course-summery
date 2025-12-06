import pandas as pd

ename = []
ework = []
eex = []
esal = []
enum = []
eemail = []

database = {
    "Employee Name": [],
    "Employee work": [],
    "Employee Experience": [],
    "Employee salary": [],
    "Employee number": [],
    "Employee E-mail": []
    }
    #

newdatabase = pd.DataFrame(database)
df = newdatabase.to_csv('Company.csv',index=False)

print("Database is sucsessfulli created !!")
