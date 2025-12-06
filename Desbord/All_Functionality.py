import pandas as pd
import csv
import plotly.express as px


def insert_row():
    ename = []
    ework = []
    eex = []
    esal = []
    enum = []
    eemail = []

    database = {
        "Employee Name": ename,
        "Employee work": ework,
        "Employee Experience": eex,
        "Employee salary": esal,
        "Employee number": enum,
        "Employee E-mail": eemail
    }
    hope = 1
    while hope == 1:
        ename = str(input("Enter the Employee Name : "))
        ework = str(input("Enter the Employee work : "))
        eex = int(input("Enter the Employee Experience : "))
        enum = int(input("Enter the Employee salary : "))
        esal = int(input("Enter the Employee number : "))
        eemail = str(input("Enter the Employee E-mail : "))

        new_row = [ename,ework,eex,esal,enum,eemail]

        file_path = 'Company.csv'
        with open(file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(new_row)

        appruvel = input("if you want add more data so enter yes otherwise no : ")
        if appruvel == "yes":
            hope = 1
        else:
            hope = 0

def deshbord():
    database = pd.read_csv("Company.csv")
    # print(Database.head())
    # print(Database.isnull().sum())
    # print(Database.describe())

    heigthest_reated = database.sort_values(by="Employee salary", ascending=False)
    heigthest_reated = heigthest_reated.head(10)
    # print(Heigthest_reated['Product Name'])

    iphone = heigthest_reated['Employee Name'].value_counts()
    graph = iphone.index
    count = heigthest_reated['Employee salary']

    figure = px.bar(heigthest_reated, x=graph, y=count, title="Employee salary chart of company")

    figure.show()

if __name__ == "__main__":
    # value = True
    # while value!=False:
    #     print(f"1. create \n2. insert\n3. chart\n4. exit")
    #     choice = (int(input("Enter Your choice : ")))
    #     match choice:
    #         case 1:
    #             pass
    #         case 2:
    insert_row()
            # case 3:
            #     deshbord()
            # case 4:
            #     break