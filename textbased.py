def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room with two doors.")
    print("One door leads to treasure, while the other leads to a monster.")
    print("Can you find the treasure and escape safely?")


def choose_door():
    while True:
        choice = input("Which door do you choose? (left/right): ").lower()
        if choice in ["left", "right"]:
            return choice
        else:
            print("Invalid choice! Please choose 'left' or 'right'.")


def encounter(choice):
    if choice == "left":
        print("\nYou enter a room filled with gold and jewels!")
        print("Congratulations, you found the treasure!")
    elif choice == "right":
        print("\nYou enter a room and a monster appears!")
        print("The monster attacks you. Game over!")


def play_game():
    intro()
    choice = choose_door()
    encounter(choice)


# Start the game
if __name__ == "__main__":
    play_game()
