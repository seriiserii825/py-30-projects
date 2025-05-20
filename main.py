from generatePassword import generatePassword


def menu():
    print("1.Generate password")
    print("2.Check password")

    choose = input("Choose an option: ")
    if choose == "1":
        generatePassword()
    else:
        print("Invalid option. Please try again.")
        menu()

if __name__ == '__main__':
    menu()
