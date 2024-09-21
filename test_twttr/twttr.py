def main():
    user = input('Input: ')
    print(shorten(user))

def shorten(word):
    mapping = { 'A':'','E':'', 'I':'', 'O':'', 'U':'', 'a':'', 'e':'', 'i':'', 'o':'', 'u':''}
    for k, v in mapping.items():
        word = word.replace(k, v)
    return word

if __name__ == "__main__":
    main()
