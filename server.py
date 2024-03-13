import socket
from number_game import NumberGame, GuessResult
from constants import HOST, PORT
from random import randint

game = NumberGame(randint(1, 100))

# default family=AF_INET, type=SOCK_STREAM
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = b""
    with conn as c:
        print(f"connected to {addr}")
        while True:
            d = c.recv(4096)
            if not data:
                break
            data += d
        guess_numb = int.from_bytes(data)
        try:
            guess_result = game.guess(guess_numb)
        except ValueError:
            conn.sendall(int.to_bytes(GuessResult.GUESS_ERROR))
        if guess_result:
            conn.sendall(int.to_bytes(guess_result))
