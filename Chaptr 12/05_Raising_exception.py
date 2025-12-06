a = int(input("Ente first value : "))
b = int(input("Enter seconde value : "))

if(a == 0):
    raise ZeroDivisionError("please Enter value wich is not 0 at the first place ")

elif(b == 0):
    raise ZeroDivisionError("please Enter value wich is not 0 at the second place ")

else:
    print(f"The Division is {a/b}")