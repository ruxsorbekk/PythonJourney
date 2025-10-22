import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print("Bagels game")
    
    while True:
        secretNum = getNumber()
        print('''When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.
              
I have thought up a number
              ''')
        
        
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('>')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))
        print('Do you want to play again? (y or n)')
        if input('>').startswith('n'):
            break
    print('Thanks for playing')


def getNumber():
    numbers = list('0123456789')
    random.shuffle(numbers)

    number = ''
    for i in range(NUM_DIGITS):
        number += numbers[i]
    
    return number

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(secretNum)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()