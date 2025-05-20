from extractTextFromImage import extractTextFromImage
from generatePassword import generatePassword


def menu():
    print("1.Generate password")
    print("2.Extract text from image")

    choose = input("Choose an option: ")
    if choose == "1":
        generatePassword()
    elif choose == "2":
        extractTextFromImage()
    else:
        print("Invalid option. Please try again.")
        menu()

if __name__ == '__main__':
    menu()
