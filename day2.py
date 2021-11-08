#rock paper scissors game Methode 2
#100days of code
#Day2  : in this day i code the rock paper scissors with a different way without using functions
import random
replay="y"
while replay =="y":
    user = input("inter 'r' for rock or 'p' for paper or 'c' for cisor :  \n " )


    if user == "r" :
        user ="rock"
        print ("you choose rock")

    elif user == "p" :
        user ="paper"
        print ("you choose paper")

    elif user == "c" :
        user ="scissors"
        print ("you choose scissors")
        
    else :
         print ("wrong choice")
    computer = random.choice(["rock" ,"paper" ,"scissors"]) 
    print(f"comuter choose {computer}")


    if computer == user : 
        print(" equals ")

    elif ( computer =="scissors"  and user == "paper" ) or (computer =="rock"  and user == "scissors")\
    or (computer =="paper"  and user == "rock") :
        print(f" you loose")

    else :
        print(f" you win ")


    replay= input("do you want play again? y or n \n")
    

else:
       print("good bye") 
