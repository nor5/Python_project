#guess the number game 
#100days of code
#Day4  : in this day i code  "guess the number " game ,
##the computer try  to guess wich number the user choose
import random
def guess(x):
           answer = "d"
      
         
           start = input(f"guess a number in your mind bitween 1 an {x} enter go if you finich : \n" )
           if start == "go":
             number = random.randint(1,x)
             answer= input (f"did you choose {number}, if it's to high press 'H' or, if it's to low press 'L'  and 'C' if it's correct : \n").lower()
             while answer !="c":
                 
                 if answer =="h":
                    number -=1
                    answer= input (f" did you choose {number}, if it's to high press 'H' or, if it's to low press 'L' ,and 'C' if it's correct : \n ").lower()

                 elif answer =="l":
                    number += 1
                    answer= input (f"did you choose {number}, if it's to high press 'H' or, if it's to low press 'L' and if it correct press 'C'  : \n ").lower()

             else:
                    print("the computer knows what is in your mind")

          
guess(10)
