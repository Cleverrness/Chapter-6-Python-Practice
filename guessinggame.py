import random

def main():
    header()

    mm_count = random.randint(1, 100) #determine the size of the jar before passing it to the function
    attempt_limit = 5

    guess(mm_count, attempt_limit)

def header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")
    print("Guess the number of M&Ms and you get lunch on the house!")
    print()

def guess(mm_count, attempt_limit):

    attempts = 0

    while attempts < attempt_limit:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)
        attempts += 1

        if mm_count == guess:
            print(f"You got a free lunch! It was {guess}.")
            break
        elif guess < mm_count:
            print("Sorry, that's too LOW!")
        else:
            print("That's too HIGH!")

    print(f"Sorry you lost, correct answer was {mm_count}!")

if __name__ == '__main__':
    main()
