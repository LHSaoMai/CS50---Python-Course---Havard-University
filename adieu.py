import sys
import inflect

p = inflect.engine()


def main():
    name = []
    while True:
        try:
            user_name = input('Name: ')
            name.append(user_name)
        except EOFError:
            break

    print('Adieu, adieu, to', p.join(name))



    #whiluser_name != '':
        #name = []
        #name.append(user_name)
       # user_name = input('Name: ')

        #return p.join(name)

main()
