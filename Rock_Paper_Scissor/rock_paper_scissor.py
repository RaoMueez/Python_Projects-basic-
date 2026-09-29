import random

# Print Rules :
print("\n----------- WELCOME TO ROCK-PAPER-SCISSOR GAME -----------\n")

print("----- RULES -----")
print("1.Rock defeats Scissors.")
print("2.Scissors defeats Paper.")
print("3.Paper defeats Rock.")
print("4.If both players choose the same option, the round ends in a draw.")

choices = ["rock", "paper", "scissor"]

while True :
    # asks for user input :
    print("\nChoose any number:")
    print("1 for Rock")
    print("2 for Paper")
    print("3 for scissor")

    # validate user's input :
    try :
        user_choice = int(input("\nEnter your choice:"))
    except ValueError :
        print("Please enter a valid input.")
        continue

    while user_choice<1 or user_choice>3 :
        user_choice = int(input("\nEnter your choice(1,2,3):"))

    user_option = choices[user_choice-1]
    print(f"\nUser's choice : {user_option}")

    # Computer's choice :
    computer_choice = random.randint(1,3)
    computer_option = choices[computer_choice-1]
    print(f"Computer's choice : {computer_option}")

    # Deciding the winner :
    if user_choice == computer_choice :
        print("\n<== It's a draw ==>")
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        print("<== User Wins! ==>")        
    else :
        print("\n<== Computer Wins ==>")

    play_again = input("\n\nDo you want to play again(y,n):").lower()
    if play_again == "n" :
        break

print("\nThank you playing.")
    