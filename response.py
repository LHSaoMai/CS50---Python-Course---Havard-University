from validator_collection import validators, checkers, errors


def main():
    email = input("What's your email adress? ")

    is_email_address = checkers.is_email(email)

    if is_email_address:
        print('Valid')
    else:
        print('Invalid')

if __name__ == "__main__":
    main()
