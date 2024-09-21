def main():
    say=input("Write something, please ")
    smile(say)

def smile(emoji):
    emoji=emoji.replace(":)","🙂")
    emoji=emoji.replace(":(","🙁")
    print(emoji)

main()
