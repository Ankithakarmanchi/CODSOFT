import random
print("---Task 4: Rock,Paper,Scissors Game---")
print("Instructions: Choose your move by typinh 'rock','paper',or 'scissor\n'")
print("Rock beats Scissor,Scissors beat paper,Paper beats Rock\n")
user_score=0
computer_score=0
choices=["rock","paper","scissors"]
while True:
    user_choices=input("Yours choice:").strip().lower()
    if user_choices not in choices:
        print("Invalid choice.Try again")
        continue
    computer_choices=random.choice(choices)
    print("computer choice:",computer_choices)
    if user_choices == computer_choices:
        print("It's a tie!")
    elif (user_choices=="rock" and computer_choices=="scissors") or \
    (user_choices=="scissors" and computer_choices=="paper") or \
    (user_choices=="paper" and computer_choices=="rock"):
        print("you Won...!\n Computer lose ")
        user_score+=1
    else:
        print("you Lose...!\n Computer won")
        computer_score+=1
    print("score --> you:",user_score,"|computer:",computer_score)
    play_again=input("Do you want to play again if yes ,enter y else, enter n?(y/n):").lower()
    if play_again!='y':
        print("Final score --> you:",user_score,"|Computer:",computer_score)
        print("Thank you for playing...!")
        break
    
