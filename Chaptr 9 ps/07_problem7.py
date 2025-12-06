with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"present {lineno}")
        break
    lineno += 1
else:
    print("absent")

print(line)