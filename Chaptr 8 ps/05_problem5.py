def peturn(n):
    if(n == 0):
        return
    print("*" * n)
    peturn(n-1)


num = int(input("Enter a number : "))
print(peturn(num))