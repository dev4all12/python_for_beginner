# rock paper scissor ex-2
import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
game_image = [rock, paper, scissors]
user_inp = int(input("Enter one values:0-Rock,1-Paper,2-Scissor:  "))
print("User Input")
# user_inp = 2
if user_inp >= 3 or user_inp < 0:
    print("You enter invalid value,'You Loss'")

else:
    print(game_image[user_inp])
    com_inp = random.randint(0, 2)
    print("Computer Input")
    print(game_image[com_inp])

    if user_inp == com_inp:
        print("Game Tie")
    elif com_inp == 0 and user_inp == 2:
        print("Computer Win")
    elif user_inp == 0 and com_inp == 2:
        print("User Win")
    elif user_inp > com_inp:
        print("User win")
    elif com_inp > user_inp:
        print("Computer win")
