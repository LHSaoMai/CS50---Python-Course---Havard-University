def main():
    sentence = input("Please write something: ")
    slow(sentence)

def slow(to):
    print(to.replace(" ","..."))

main()
