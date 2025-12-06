with open("poem.txt") as f:
    c = f.read()
    if("twinkal" in c):
        print("is here")
    else:
        print("is not here")