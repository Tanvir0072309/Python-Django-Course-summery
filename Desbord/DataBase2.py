import csv
hope = 1
while hope == 1:
    name = str(input("Enter your name : "))
    deg = str(input("Enter your degree : ")).upper()
    year = int(input("Enter passing year : "))
    mark = float(input("Enter passing marks : "))

    new_row = [name,deg,year,mark]

    file_path = 'DataBase01.csv'
    with open(file_path,mode='a',newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(new_row)

    appruvel = input("if you want add more data so enter yes otherwise no : ")
    if appruvel == "yes":
        hope = 1
    else:
        hope = 0