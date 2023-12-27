import random

def game_of_21():
    player_score = 0
    while player_score < 21:
        player_choice = input("Do you want to draw another card? (yes/no) ")
        if player_choice.lower() == "yes":
            card_value = random.randint(1, 10)
            print(f"You drew a card with value {card_value}.")
            player_score += card_value
            print(f"Your current score is {player_score}.")
        elif player_choice.lower() == "no":
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if player_score == 21:
        print("You win!")
    elif player_score > 21:
        print("Bust! You lose.")
    else:
        print("You stopped at a score less than 21.")

game_of_21()
