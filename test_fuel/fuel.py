def main():
    fraction = input('Fraction : ')
    number = convert(fraction)
    print(gauge(number))

def convert(fraction):
    try:
        x,y = fraction.split('/')
        return round(int(x)/int(y)*100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <=1:
        return 'E'
    elif percentage >=99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == '__main__':
    main()
