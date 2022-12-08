# library yang digunakan
from random import randint

#variabel yang digunakan
var = ["ROCK","PAPER","SCISSOR"]

#pilihan acak computer
com = var[randint(0,2)]
player = False

while player == False:
    player = input("choose rock(1), paper(2) or scissors(3)  : ").upper()
    if player == com:
        print("Tie!!!")
    elif player == 'ROCK':
        if com == 'PAPER':
            print("YOU LOSE!!!",com, "AGAINTS",player)
        else:
            print("YOU WIN!!!",player, "AGAINTS",com)
    elif player == 'PAPER':
        if com == 'SCISSORS':
             print("YOU LOSE!!!",com, "AGAINTS",player)
        else:
            print("YOU WIN!!!",player, "AGAINTS",com)
    elif player == 'SCISSORSS':
        if com == 'ROCK': 
            print("YOU LOSE!!!",com, "AGAINTS",player)
        else:
            print("YOU WIN!!!",player, "AGAINTS",com)
player = False
com = var[randint(0,2)]