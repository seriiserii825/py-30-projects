from checkPasswords import checkPasswords
from checkWebsitesStatus import checkWebsitesStatus
from extractTextFromImage import extractTextFromImage
from generatePassword import generatePassword
from rich import print

from guessPassword import guessPassword


def menu():
    print("[green]1.Generate password")
    print("[blue]2.Extract text from image")
    print("[green]3.Check websites status")
    print("[blue]4.Check passwords")
    print("[green]5.Guess passwords")

    choose = input("Choose an option: ")
    if choose == "1":
        generatePassword()
    elif choose == "2":
        extractTextFromImage()
    elif choose == "3":
        checkWebsitesStatus()
    elif choose == "4":
        checkPasswords()
    elif choose == "5":
        guessPassword()
    else:
        print("Invalid option. Please try again.")
        menu()

if __name__ == '__main__':
    menu()
