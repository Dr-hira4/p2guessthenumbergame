# Project 2 : guess the number game by computer
# 1 to 100 numbers.



import random
def guess_the_number_game():
    """Project 2: Guess the Number Game by Computer"""
    number = random.randit(1, 100)
    guesses_left = 7
    #welcome message
    print("welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")

   
    #loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses_left. ")
        try:
            guess = int(input("Take a guess of another number."))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue
        
         #guess the secret number
        if guess < number:
            print("Too low number . Tell another!")
        elif guess > number:
            print("Too high number , Tell another!")
        else: 
            print(f"Congratulations! you got the correct number in {7 - guesses_left + 1} tries.")
        return # Exit the game
        
    guesses_left -= 1
    #when all guesses will be finished
    print(f"/nYou ran out of guess . The number was {number}.") 


    
    guess_the_number_game()
