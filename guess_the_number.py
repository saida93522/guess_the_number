import random

correct = 'you guessed correctly!'

too_low = 'Too Low!!!'

too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 1000


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    try:
        return int(input('Guess the secret number? '))

    except ValueError:
        print('Please try again,enter only a number')


def check_guess(guess, secret, counter):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct, counter
    if guess < secret:
        counter += 1
        return too_low, counter
    if guess > secret:
        counter += 1
        return too_high, counter


def main():
    play = input("Press 'Y' to play or Enter to quit ")

    while play.lower() == 'y':
        (low, high) = configure_range()
        secret = generate_secret(low, high)

        number_of_guesses = 1  # count how many times user tried to guess
        while True:
            guess = get_guess()
            (result, number_of_guesses) = check_guess(
                guess, secret, number_of_guesses)
            print(result)

            if result == correct:
                print(f'It took you {number_of_guesses} tries to guess it')
                break
        play = input("Press 'Y' to play again or Enter to quit ")

    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
