logo="""

  _   _                 _                  _____                     _                _____                       
 | \ | |               | |                / ____|                   (_)              / ____|                      
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___  
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___| 
                                                                              __/ |                               
                                                                             |___/                                

"""
import random

def check_guess(guess):
    global win,attempts
    if guess==num:
        win=True
    else:
        attempts-=1
        if attempts==0:
            print("You lose, better luck next time.")
        else:
            if num>guess:
                print("The number is greater")
            else:
                print("The number is smaller")

print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.")

level= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level=="easy":
    print("You have 10 attempts to guess the number")
    attempts=10
elif level=="hard":
    print("You have 5 attempts to guess the number")
    attempts=5

num=random.randint(1,100)
win=False 


while attempts!=0 and win==False:
    guess=int(input("Make a guess: "))
    check_guess(guess)

if win==True:
    print("You won congratulations!")