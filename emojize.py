import emoji
#def main():
    #english = input('Input : ')
    #print(f'Output : {emoji.emojize(english,language='alias')}')

#main()

def main():
    english = input('Input : ')
    print(f'Output : {emo(english)}')

def emo(x):
    return emoji.emojize(x,language='alias')

main()
