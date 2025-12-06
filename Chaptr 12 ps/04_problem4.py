try:
    a = int(input("Enter the First number : "))
    b = int(input("Enter the Second number : "))
    print(a/b)


except ZeroDivisionError as v:
    print("Infinite")
