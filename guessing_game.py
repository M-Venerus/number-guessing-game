import random

def start_difficulty():
    """Print beginning statement of guessing_game then get input for difficulty level."""
    print("The computer will choose a number between 1 and 100 at random. You have to guess it.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == "easy":
        return 10
    else:
        return 5

def randomNum():
    """Generate random integer between 1 and 100."""
    num = random.randint(1, 100)
    return num

def guess(attempts, hidden_number):
    """Take a guess from user and compare it with a hidden number. User may guess again until
    attempts run out. Return bool for guess if correct or if attemps run out."""
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
    """Informs user if they won or lost."""
    if win_or_lose:
        print(f"You got it! You win! The number is {randomNum_selected}!")
    else:
        print(f"You are out of guesses, you lose. The number was {randomNum_selected}.")

randomNum_selected = randomNum()
starting_attempts = start_difficulty()
win_or_lose = guess(starting_attempts, randomNum_selected)
conclusion(win_or_lose)