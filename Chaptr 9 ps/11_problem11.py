# first i copy this file in a diffrent file and than delet the previos file
with open("this.txt") as f:
    contant= f.read()

with open("this_copy.txt", "w") as f:
    f.write(contant)