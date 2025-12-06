try:
    a = int(input("Enter your input : "))
    print(a)

except ValueError as v:
    print("sahi karo jao vapas se")

except Exception as e:
    print("please Enter a integer value")