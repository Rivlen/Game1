from random import randint


def guess_the_number():
    roll = randint(1, 100)
    while True:
        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except ValueError:
                print("It's not a number!")

        if guess < roll:
            print("Too small!")
            continue

        elif guess > roll:
            print("Too big!")

        elif guess == roll:
            print("You win!")
            return None


if __name__ == '__main__':
    guess_the_number()
