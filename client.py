import socket
from number_game import GuessResult
from constants import HOST, PORT

guess_result = 999

while guess_result != GuessResult.GUESS_CORRECT:
    with socket.socket() as s:
        s.connect((HOST, PORT))
        guess = ""
        while not guess:
            guess = input("What number would you like to guess?\n")
            try:
                int(guess)
            except:
                print("Please enter a valid Integer")
        s.sendall(int.to_bytes(guess, 'little'))
        data = int.from_bytes(s.recv(2), 'little')
        if data == GuessResult.GUESS_CORRECT.value:
            print(f"Correct! The number was {data}")
            break
        if data == GuessResult.GUESS_TOO_LARGE.value:
            print(f"Your guess was too large :(")
        if data == GuessResult.GUESS_TOO_SMALL.value:
            print(f"Your guess was too small :(")
        if data == GuessResult.GUESS_CORRECT.value:
            print(f"There was an error with your guess on the server side")