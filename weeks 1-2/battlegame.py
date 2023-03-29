
wizard = "wizard"
elf = "elf"
human = "human"

human_hp = 150
elf_hp = 100
wizard_hp = 70

wizard_damage = 150
human_damage = 20
elf_damage = 100

dragon_hp = 300
dragon_damage = 50
gameIsOn = "y"

while gameIsOn == "y":
    while True:
        print(f"1) {wizard}")
        print(f"2) {elf}")
        print(f"3) {human}")
        print("Type exit to quit game")
        character_choice = input("Choose a character: ")
        if character_choice == "1" or character_choice.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character_choice == "2" or character_choice.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character_choice == "3" or character_choice.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        else:
            print("Unknown character, please pick a valid choice! 1, 2 or 3")

    print(f"You have chosen to be a {character}")
    print(f"Helath: {my_hp}")
    print(f"Damage: {my_damage}")

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print(f"the dragon HP is now: {dragon_hp}\n")
        if dragon_hp <= 0:
            print("You have defeated the dragon!")
            break
        else:
            my_hp = my_hp - dragon_damage
            print(f"The {character}  was damaged by the dragon")
            print(f"the {character} HP is now: {my_hp}\n")
            if my_hp <= 0:
                print(f"The {character} have been defeated by the dragon!")
                break
    gameIsOn = input("Do you want to play again? y or n\n")
    if gameIsOn == "y":
        dragon_hp = 300

print("Game is off! Thank you for playing")
