with open("this.txt") as f:
    contant= f.read()

with open("this_copy.txt", "w") as f:
    f.write(contant)