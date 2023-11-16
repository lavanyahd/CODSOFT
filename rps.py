import random
u_score=0
c_score=0
print("------------Welcome to rock,paper and scissor game!-----------------" )
print("Lets start the game!")
while True:
   
    user_choice=input("Please choice rock,paper,scissor or quit:").lower()
    if user_choice=='quit':
        break
    if user_choice not in['rock','paper','scissor']:
        print("Invalid choice please eneter correct choice")
        continue
    computer_choice=random.choice(['rock','paper','scissor'])
    print(f"Computer choice::{computer_choice}")
    if user_choice==computer_choice:
        print("Tie")
    elif(user_choice=='rock' and computer_choice=='scissor' or  user_choice=='paper' and computer_choice=='rock' or  user_choice=='scissor' and computer_choice=='paper'):
        print("You win")
        u_score+=1
    else:
        print("computer wins")
        c_score+=1
    print(f"User score{u_score},Computer score{c_score}")    
         
    
        
                      
