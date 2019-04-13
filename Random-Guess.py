
import random
number=random.randint(0,30)
print('Real Number is {}.'.format(number))

while True:
    guess=input('Guess the number= ')
    if guess.isdigit() is True:
        print('Processing...')    
        value = int(guess)
        if value == number:
            print('Correct!')
            break
        else:
            print('Sorry! TRY AGAIN...')
    else:
        print('Enter a number')
