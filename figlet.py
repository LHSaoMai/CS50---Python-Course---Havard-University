from pyfiglet import Figlet
import sys
import random


def main():
    print(words())

def words():
    figlet = Figlet()
    if len(sys.argv)==1:
        word = input('Input: ')
        x=random.randint(0,len(figlet.getFonts()))
        fonts=figlet.getFonts()[x]
        figlet.setFont(font=fonts)
        return figlet.renderText(word)
    elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font') and (sys.argv[2] in figlet.getFonts()):
        word = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        return figlet.renderText(word)
    else:
        sys.exit('Invalid usage')



main()
