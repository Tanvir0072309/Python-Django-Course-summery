def table(n):
    for i in range(1,10):
        print(f"{n} * {i} = {n*i}")

number = int(input("Enter a number : "))
print(table(number))