def main():
    prompt = fuel()
    print(prompt)

def fuel():
    while True:
        try:
            fraction = input('Fraction : ')
            number = round(int(fraction.split('/')[0])/int(fraction.split('/')[1])*100)
            if 1 < number < 99:
                return f"{number}%"
            elif number <= 1 :
                return 'E'
            elif number > 100:
                pass
            else:
                return 'F'
        except (ZeroDivisionError,ValueError):
            pass

main()
