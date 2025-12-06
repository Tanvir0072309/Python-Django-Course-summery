with open("this.txt") as f:
    contant1= f.read()

with open("this_copy.txt") as f:
     contant2= f.read()

if(contant1 == contant2):
    print("Yes both are identical")
else:
    print("No both are not identical")