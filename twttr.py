def main():
    user = input('Input: ')
    print(transform(user))

def transform(to):
    mapping = { 'A':'', 'E':'', 'I':'', 'O':'', 'U':'', 'a':'', 'e':'', 'i':'', 'o':'', 'u':''}
    for k, v in mapping.items():
        to = to.replace(k, v)
    return to

main()
