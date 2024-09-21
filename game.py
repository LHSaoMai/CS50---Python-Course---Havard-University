import random
import sys
def main():
    number = user_choice()
    while True:
        try:
            guess=int(input('Guess: '))
            if guess > number:
                print('Too large!')
            elif guess < number:
                print('Too small!')
            elif guess == number:
                sys.exit("Just Right!")
                break
        except ValueError:
            pass

def user_choice():
        while True:
            try:
                n=int(input('Level : '))
                if n<0:
                    continue
                else:
                    number = random.randint(1,n)
                    return number
            except ValueError:
                pass
main()
