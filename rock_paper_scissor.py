
"""
A-ROCK
rock-tie
scissor-rock win
paper-paper win

B-SCISSOR
rock-rock win
scissor-tie
paper -scissor win

C-PAPER
rock-paper win
scissor-scissor win
paper - tie

"""
import random
item_list=["Rock","Paper","Scissor"]
user_input=input("Enter your move(Rock,Paper,Scissor):").strip().capitalize()
comp_input=random.choice(item_list)
print("YOUR MOVE:",user_input  ,"COMPUTER MOVE:",comp_input)

if user_input == comp_input:
    print("TIE :)")

elif user_input == "Rock":
    if comp_input == "Scissor":
        print("YOU WIN :D ")
    else:
        print("YOU LOOSE :( \n COMPUTER WINS ") 

elif user_input=="Scissor":
    if comp_input=="Rock":
        print("YOU LOOSE :( \n COMPUTER WINS") 
    else:
        print("YOU WIN :D ")

elif user_input == "Paper":
    if comp_input == "Rock":
        print("YOU WIN :D ")
    else:
        print("YOU LOSE :( \nCOMPUTER WINS")

else:
    print("Invalid input. Please choose Rock, Paper, or Scissor.")    
         