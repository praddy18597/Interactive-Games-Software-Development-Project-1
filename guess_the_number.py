import random

def guess(x):
    # we used randint function to find out random number correctly
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry..Guess again too low')
        elif guess > random_number:
            print('sorry..Guess again too high')
    
    print(f'You have Guess the number {random_number} Correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''    #we take feedback as empty string
    while feedback != 'c':                 #we used c for correct number
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low  #could be also high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or Correct Number')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your Number, {guess}, Correctly!')
        

guess(100)