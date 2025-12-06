word = "donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("donkey.txt", "w") as f:
    f.write(contentNew)