fruit_basket = ['apple', 'strawberry', 'orange', 'avocado', 'kiwi']

user_guess = input('Guess a fruit name: ')

if user_guess in fruit_basket:
    print('Your guess is correct!')
else:
    print('You guessed wrong. Try again.')
