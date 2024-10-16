import random
'''
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
– Too high
– Too low
– Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
'''
def guessing_game():

    number = random.randint(0, 100)
    while s := input("Guess a number ").isdigit():
        user_int = int(s)

        if user_int > number:
            print("Too high")
        elif user_int < number:
            print("Too low")
        else:
            print("Just right")
            break

# guessing_game()
name = 'world'
first = 'Reuven'
last = 'Lerner'
print(f'Hello, {first:#<10} {last:#>10}')
