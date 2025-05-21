import string
import time
import itertools

def bruteForce(word: str, length: int):
    chars: str = string.ascii_lowercase
    have_digits = input("Do you want to include digits? (y/n): ")
    if have_digits == "y":
        chars += string.digits

    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        guess = ''.join(guess)
        attempts += 1
        print(f"Trying: {guess}")
        if guess == word:
            print(f"Password found: {guess}")
            print(f"Attempts: {attempts}")
            return

    

def guessPassword():
    word: str = input("Enter the password to guess: ")
    length: int = len(word)
    start_time = time.time()
    bruteForce(word, length)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    

if __name__ == '__main__':
    guessPassword()
