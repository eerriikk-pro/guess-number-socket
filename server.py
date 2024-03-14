import socket
from number_game import NumberGame, GuessResult
from constants import HOST, PORT, MAX_BYTES
from random import randint

game = NumberGame(randint(1, 100))

# default family=AF_INET, type=SOCK_STREAM
with socket.socket() as s:
    # for testing so socket resets right after rerun
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        data = b""
        with conn as c:
            print(f"connected to {addr}")

            data = c.recv(MAX_BYTES)
            print(data)
            guess_numb = int.from_bytes(data, byteorder='little')
            try:
                guess_result = game.guess(guess_numb)
            except ValueError:
                conn.sendall(GuessResult.GUESS_ERROR.value.to_bytes(2, byteorder='little'))
            if guess_result:
                conn.sendall(guess_result.to_bytes(1, byteorder='little'))
