import random
# import keyboard as k


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("press Enter to pick a card, or Q then enter to quit: ")
    if choice == "":
        newCard = random.choice(diamonds)
        hand.append(newCard)
        diamonds.remove(newCard)
        print(f"your hand: {hand}")
        print(f"Remaining cards: {diamonds}")
        if not diamonds:
            print("There are no more cards to pick")
    elif choice.lower() == "q":
        break
    else:
        print("Not a valid choice!")


# alternative way of somewhat accommplishing this challenge using
# the keyboard package to detect keyboard presses
    # if k.read_key() == "enter":
    #     newCard = random.choice(diamonds)
    #     hand.append(newCard)
    #     diamonds.remove(newCard)
    #     print(f"your hand: {hand}")
    #     print(f"Remaining cards: {diamonds}")
    #     if not diamonds:
    #         print("There are no more cards to pick")
    # elif k.read_key() == "q":
    #     break

print("goodbye")
