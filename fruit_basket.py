fruit_basket = ['apple', 'strawberry', 'orange', 'avocado', 'kiwi']


def guess_fruit(basket):
    i = 0
    while True:
        user_guess = input('Guess a fruit name: ')
        if user_guess in basket:
            print('Your guess is correct!')
            break
        else:
            print('You guessed wrong. Try again.')
            i = i + 1
            if i == 5:
                print('You have reached the max number of attempts.')
                break


def main():
    guess_fruit(fruit_basket)


main()
