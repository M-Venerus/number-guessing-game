import random

def attempts_start():
    print("The computer will choose a number between 1 and 100 at random. You have to guess it.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == "easy":
        return 10
    else:
        return 5

def randomNum():
    num = random.randint(1, 100)
    return num

def guess(attempts, hidden_number):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the numer.")
        current_guess = int(input("Make a guess: "))
        if current_guess == hidden_number:
            return True
        elif current_guess > hidden_number:
            print("Too high.")
        elif current_guess < hidden_number:
            print("Too low.")
        print("Guess again.")
        attempts -= 1
    return False
    
def conclusion(win_or_lose):
    if win_or_lose:
        print(f"You got it! You win! The number is {randomNum_selected}!")
    else:
        print(f"You are out of guesses, you lose. The number was {randomNum_selected}.")

randomNum_selected = randomNum()
starting_attempts = attempts_start()
win_or_lose = guess(starting_attempts, randomNum_selected)
conclusion(win_or_lose)