import re


def main():
    camel =input("camelCase: ")
    print("snake_case :",snakecase(camel))

def snakecase(snake):
    List = re.findall('.[^A-Z]*', snake)
    word= '_'.join(List).lower()
    return word

main()
