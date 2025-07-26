import random

def guess_num():
    print('...WELCOME TO NUMBER GUESSING GAME...')
    print('...Guess a number between 1 and 100...')
    
    sec_num = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input('Enter Your Guess: '))
            attempts +=1

            if guess < 1 or guess > 100:
                print('ERROR! Please Guess a Number Between 1 and 100')
            elif guess < sec_num:
                print('TOO LOW!!! Try Again!')
            elif guess > sec_num:
                print('TOO HIGH!!! Try Again!')
            else:
                print(f'CONGRATULATIONS! Your guessed number is in {attempts} attempts.')
                break
        except ValueError:
            print('Invalid input! Please enter a number')
            
if __name__ == "__main__":
    guess_num()