import random

def main():
    level= get_level()
    score = 0
    attempts = 0
    for _ in range(10):
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        answer = number1 + number2
        attempts = 0
        while attempts < 3:
            try:
                question = int(input(f"{ number1} + {number2} = "))
                answer = number1 + number2
                if question == answer:
                    score = score + 1
                    break
                else:
                        print("EEE")
                        attempts = attempts + 1
            except ValueError:
                        print("EEE")
                        attempts = attempts + 1
            if attempts == 3:
                        print(f"{number1} + {number2} = {answer}")


    print(f"Score: {score}")


def get_level():
    #this get the lebel digit (so if 1 only 1 level digit etc)
    while True:
            try:
                level = int(input('Level: '))
                if level in (1, 2, 3):
                    return level
            except ValueError:
                  pass



def generate_integer(level):
    #for i in range(10):
    if level == 1:
        range_start = 10**(level-1)-1
        range_end = (10**level)-1
        return random.randint(range_start, range_end)
    elif level in (2,3):
        range_start = 10**(level-1)
        range_end = (10**level)-1
        return random.randint(range_start, range_end)
    #else:
      #  raise ValueError


        #second_number =random.randint(range_start, range_end)
        #number = random.append(first_number)
        #random_n2.append(second_number)
        #i = i + 1


if __name__ == "__main__":
      main()
