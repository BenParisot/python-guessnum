import random

print('-------------------------------------')
print('--------GUESS THAT NUMBER GAME-------')
print('-------------------------------------')
print();

the_number = random.randint(0, 100)

guess_int = -1

while guess_int != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_int = int(guess_text)

    if guess_int < the_number:
        print('Your guess is too low')
    elif guess_int > the_number:
        print('Your guess is too high')
    else:
        print('You win!')

print('done')