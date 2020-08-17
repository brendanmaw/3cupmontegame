from random import shuffle

# Initial List, adding in a comment here to test git commands.
mylist = ['', 'O', '']


def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)


def player_guess():

    guess = ''

    while guess not in ['0', '2', '1']:
        guess = input(
            'Pick a number between 0-2, if you find the ball, you win! ')
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print('Wrong guess!')
        print(mylist)


# Shuffle List
shuffled_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
check_guess(shuffled_list, guess)
