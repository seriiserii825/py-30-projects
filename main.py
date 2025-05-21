from checkPasswords import checkPasswords
from checkWebsitesStatus import checkWebsitesStatus
from downloadImage import downloadImage
from extractTextFromImage import extractTextFromImage
from generatePassword import generatePassword
from rich import print

from guessPassword import guessPassword
from sortFiles import sortFiles


def menu():
    print("[green]1.Generate password")
    print("[blue]2.Extract text from image")
    print("[green]3.Check websites status")
    print("[blue]4.Check passwords")
    print("[green]5.Guess passwords")
    print("[blue]6.Download Image")
    print("[green]7.Sort files")

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
    elif choose == "6":
        downloadImage()
    elif choose == "7":
        sortFiles()
    else:
        print("Invalid option. Please try again.")
        menu()

if __name__ == '__main__':
    menu()
