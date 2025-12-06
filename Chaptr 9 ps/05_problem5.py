word = ["donkey", "ganda", "bhai"]

with open("donkey.txt", "r") as f:
    content = f.read()

for word in word:
    content = content.replace(word,"#"*len(word))

with open("donkey.txt", "w") as f:
    f.write(content)