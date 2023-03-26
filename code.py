# Project
import random
import time
print("\nWelcome to Rock Paper Scissor Game. \nBy Sahil, Sahil Saharan , Saket Bansal \n")
time.sleep(2)
name = input("Enter your Name: ")

print("Hello " + name + "! Best of Luck!")
time.sleep(2)

print("The game is about to start!\n Let's play Rock Paper Scissor!")
time.sleep(1)

n=(int(input('Enter The Number of Rounds: ')))
i=1
print()
You_score=0
Computer_score=0
Tie_score=0
while(i<=n):
    You = input("Select Rock, Paper, or Scissor: ").lower()
    Computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Computer selected: ", Computer)

    if You == "rock" and Computer == "paper":
        print("Computer Won")
        Computer_score +=1
    elif You == "paper" and Computer == "scissor":
        print("Computer Won")
        Computer_score +=1
    elif You == "scissor" and Computer == "rock":
        print("Computer Won")
        Computer_score +=1
    elif You == Computer:
        print("Tie")
        Tie_score +=1
    else:
        print("You Won")
        You_score +=1
    i+=1
print()
print("Game Score :-")
print(name,"'s score is :", You_score)
print("Computer's score is :", Computer_score)
print("Tie :", Tie_score )