import random

print('-------------------------------------')
print('--------GUESS THAT NUMBER GAME-------')
print('-------------------------------------')
print();

the_number = random.randint(0, 100)

guess_int = -1

name = input('What is your name?')

while guess_int != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_int = int(guess_text)

    if guess_int < the_number:
        print('Sorry {}, your guess is too low'.format(name))
    elif guess_int > the_number:
        print('Sorry {}, your guess is too high'.format(name))
    else:
        print('You win, {}! The correct number was {}'.format(name, guess_int))

print('done')