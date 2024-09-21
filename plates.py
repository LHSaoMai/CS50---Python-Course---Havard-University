import re
import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    number_and_letter = re.findall(r"[A-Za-z]+|\d+",s)
    punctuation = any(i in string.punctuation for i in s)
    length = len(s)
    two_first_letter = []
    for i in s:
        if i.isalpha() == True:
            two_first_letter.append(True)
        else:
            two_first_letter.append(False)

    if (length<=6 and length >= 2):
        if len(number_and_letter)==2:

            if two_first_letter[0]==True and two_first_letter[1]==True :
                if (number_and_letter[1][0] != '0') and s.isspace()==False and len(number_and_letter)<=2 and punctuation==False:
                    return True
                else:
                    return False

            else:
                return False
        elif len(number_and_letter)<=2:
            if two_first_letter[0]==True and two_first_letter[1]==True :
                if s.isspace()==False and punctuation==False:
                    return True
                else:
                    return False

            else:
                return False

    else:
        return False

main()
