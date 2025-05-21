from rich import print

def checkPasswords():
    passwords: list[str] = []
    with open("data/passwords.txt", "r") as file:
        for line in file:
            passwords.append(line.strip())

    password = input("Enter the password to check: ")
    if password in passwords:
        # get index
        index = passwords.index(password)
        print(f"{password}: [red]#{index}[/red]")
    else:
        print(f"{password}: [green]Unique[/green]")
