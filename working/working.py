import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search(r"([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (PM|AM)",s):
            hours_first = int(hours.group(1))
            hours_last = int(hours.group(4))

            if hours.group(3)=='PM' and hours_first != 12:
                hours_first = hours_first + 12
            elif hours.group(6)=='PM' and hours_first != 12:
                hours_last = hours_last + 12

            if hours.group(3)=='AM' and hours_first==12:
                    hours_first = '00'
            elif hours.group(5)=='AM' and hours_last==12:
                    hours_last = '00'


            minute_first = hours.group(2)
            minute_last = hours.group(5)

            if minute_first==None:
                minute_first = '00'

            if minute_last==None:
                minute_last = '00'

            return f"{str(hours_first).zfill(2)}:{minute_first} to {str(hours_last).zfill(2)}:{minute_last}"
    else:
         raise ValueError


if __name__ == "__main__":
    main()
