import pandas as pd

name = []
deg = []
year = []
mark = []

database = {
    "Name": name,
    "Degree": deg,
    "year" : year,
    "Marks" : mark
}

hope = 1
while hope == 1:
    length = 0
    name.insert(length,str(input("Enter your name : ")))
    deg.insert(length,str(input("Enter your degree : ")).upper())
    year.insert(length,int(input("Enter passing year : ")))
    mark.insert(length,float(input("Enter passing marks : ")))

    appruvel = input("if you want add more data so enter yes otherwise no : ")
    if appruvel == "yes":
        hope = 1
    else:
        hope = 0

nerDatabase = pd.DataFrame(database)

nerDatabase.to_csv('DataBase01.csv',index=False)