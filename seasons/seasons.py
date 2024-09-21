from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birthday= input("Date of Birth : ")
    print(day(birthday))

def day(birthday):
    try:
        year,month, day= birthday.split('-')
        dates = date(int(year), int(month), int(day))
    except ValueError:
        return sys.exit("Invalid")
    today = date.today()
    diff = round((today-dates).days*24*60)
    return f"{p.number_to_words(diff,andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
