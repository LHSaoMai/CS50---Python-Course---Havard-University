import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   if numbers := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        all_number = True
        for i in numbers.groups():
            if int(i) >255:
                all_number = False

        if all_number:
            return True
        else:
             return False
   else:
       return False

if __name__ == "__main__":
    main()
