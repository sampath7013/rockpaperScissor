import random
user_choice = int(input("What do you choose? '0' for rock, '1' for paper, '2' for scissors\n"))
computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")
if user_choice>2:
    print("You typed an invalid number. You lose.")
elif computer_choice==user_choice:
    print("It's a draw")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice==2 and user_choice==0:
    print("You win")
elif computer_choice>user_choice:
    print("You lose")
elif computer_choice<user_choice:
    print("You win")   
