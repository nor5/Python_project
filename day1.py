#rock paper scissors game 
#100days of code
#Day1  : in this day i code the rock paper scissors with  using functions
import random
def start ():
    #computer = random.choice(["rock" ,"paper" ,"scissors"])
    user = input("inter 'r' for rock or 'p' for paper or 'c' for scissors : \n " )
     
    if user != "r" and user != "p" and user !=  "c" :  
             print (" wrong choice, replay" )
             return start()
    else :   
    
        if user == "r" :
               user="rock"
        if user == "p" :
                  user="paper"
        if user == "c" :
                 user="scissors"
        
        return  play(user )
        
       
def play(player):
   computer = random.choice(["rock" ,"paper" ,"scissors"])
   #user = input("inter 'r' for rock or 'p' for paper or 'c' for cisor :  \n " )
   if computer == player : 
            return computer +" vs " + player +"  equals  "
          
   elif winner(player , computer):
             return computer +"  vs  " +player +"  you won "
             
   else:
             return computer+ "  vs  "+ player +" you lost " 
             

def winner (player , adversary):
    if ( player =="c"  and adversary == "p" ) or (player =="r"  and adversary == "c")\
    or (player =="p"  and adversary == "r") :
        return True


replay="y"
while replay=="y":
      print (start())
      replay = input("do you want to play again ? n or y \n")
else:
    print(" good bye")

    




