import random
possible_actions = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
end = False

while end == False:
    user_action = input("\nEnter a choice (rock, paper, scissors): ")
    computer_action = random.choice(possible_actions)
    print("\nYou chose ",user_action ,", computer chose ", computer_action)

    if (user_action != "rock") and (user_action != "paper") and (user_action != "scissors"):
        print("Invalid choice :(")
    elif user_action == computer_action:
        print("Both players selected.", user_action ," It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            user_score += 1
            print("Rock smashes scissors! You win!")
        else:
            computer_score += 1
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            user_score += 1
            print("Paper covers rock! You win!")
        else:
            computer_score += 1
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            user_score += 1
            print("Scissors cuts paper! You win!")
        else:
            computer_score += 1
            print("Rock smashes scissors! You lose.")

    print("Total score: User",user_score ," - ", computer_score, "computer")

    end_input = str(input("\npress '0' to end the game: "))
    if end_input == '0':
        end = True