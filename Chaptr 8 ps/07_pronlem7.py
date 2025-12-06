def inserting(x,z):
    string.insert(x,z)
    return string


string = [1,2,3,4,5]
main = int(input("Enter the number which is alrady exist : "))
rep = int(input("Enter number replace : "))

print(inserting(main,rep))