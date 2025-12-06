with open("log.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("present")
else:
    print("absent")
