from validator_collection import is_email


def main():
    print(check_email(input("What's your email address?  ")))


def check_email(email):
    if is_email(email):
        return 'Valid'
    return 'Invalid'


if __name__ == "__main__":
    main()