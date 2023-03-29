import random


# function to use user input to guess a number in a given range
def guess_random_num(tries: int, start: int, stop: int):
    target_num = random.randint(start, stop)
    tries_left = tries
    won_game = False  # variable to check if number have been found and game won
    while tries_left > 0:
        print(f"You have {tries_left} tries remaining")
        guess = int(input(f"Choose a number between {start} & {stop}: "))
        if guess == target_num:
            print("You guessed right! You must be a mind reader")
            won_game = True  # switches to let program know word has been found and game is won
            break
        elif guess > target_num:
            print("Your guess is to high! Try a lower number")
            tries_left -= 1
        elif guess < target_num:
            print("Your guess is to low! Try a higher number")
            tries_left -= 1
    if won_game:  # checkes game status (win or lose)
        return
    else:
        print("No more tries remaining. Game Over!")
        return


# function to use linear search to find a randomly chosen number
def guess_random_num_linear(tries: int, start: int, stop: int):
    tries_left = tries
    target_num = random.randint(start, stop)
    num_found = False  # variable to check if number have been found
    print(f"The computer is looking for the number {target_num}")
    for num in range(stop + 1):
        if tries_left > 0:
            print(f"Tries remaining: {tries_left}")
            if num == target_num:
                print("Computer guessed the right number!")
                num_found = True  # switches to let program know word has been found
                break
            else:
                print(f"Computer guessed {num}")
                tries_left -= 1
        else:
            break
    if num_found:  # checkes the status of if the number has been found
        return
    else:
        print("No more tries remaining. Game Over!")
        return


# function to use binary search method to find a randomly generated number
def guess_random_num_binary(tries: int, start: int, stop: int):
    tries_left = tries
    target_num = random.randint(start, stop)
    num_found = False  # variable to check if number have been found
    lower_bound = start
    upper_bound = stop
    print(f"The computer is looking for the number: {target_num}")
    while lower_bound <= upper_bound:
        if tries_left > 0:
            pivot = len(range(lower_bound, upper_bound + 1)) // 2
            if pivot == target_num:
                print("Number Found!")
                num_found = True  # switches to let program know word has been found
                break
            elif pivot > target_num:
                upper_bound = pivot
                print("Guessing lower number!")
                tries_left -= 1
            elif pivot < target_num:
                lower_bound = pivot
                print("Guessing higher number!")
                tries_left -= 1
        else:
            break
    if num_found:  # checkes the status of if the number has been found
        return
    else:
        print("No more tries remaining. Game Over!")
        return


""" Task 1 driver code """
# guess_random_num(5, 0, 10)

""" Task 2 driver code """
# guess_random_num_linear(5, 0, 10)

""" Task 3 driver code """
# guess_random_num_binary(5, 0, 100)
