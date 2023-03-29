import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print(f"Current High Score: {high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter Your Choice? ")
        print('')
        if choice == "1":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            rollTotal = dice1 + dice2
            print(f"You rolled a... {dice1}")
            print(f"You rolled a... {dice2}\n")
            print(f"You have rolled a total of: {rollTotal}\n")
            if rollTotal > high_score:
                print("New Highscore!!\n")
                high_score = rollTotal
        elif choice == "2":
            break
    print("Game Off Goodbye")


dice_game()
