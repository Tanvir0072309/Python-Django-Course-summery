import random #import a randome
def game():
    print("your playing game..")
    score = random.randint(1,65)  #select any random number from defined range
    with open("hiscore.txt") as f: # Open the file as f
        hiscore = f.read() # store the value of file in hiscore
        if(hiscore!=""):
            hiscore = int(hiscore) # if hiscore is not empty so the valye of the text file is convert in to the integer
        else:
            hiscore = 0 # if is empty so it pass 0
    print(f"your score {score}")
    if(score>hiscore): # if the score value is greater than hiscore so it written in to the text file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()
