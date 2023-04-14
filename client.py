import socket
import threading
import logging
import sys

HOST = "127.0.0.1"
PORT = 12345

logging.basicConfig(
    filename="client.log", filemode="a", format="%(asctime)s - %(message)s", level=logging.INFO
)

username = input('Введите Ваш никнейм:\n')
while not username:
    username = input('Никнейм не может быть пустым. Введите никнейм:\n')


def receive():
    while True:
        try:
            data = socket.recv(1024)
            print(data.decode())
        except Exception as e:
            logging.exception(e)
            socket.close()
            break


def send():
    while True:
        try:
            msg = input()
            if msg == 'quit':
                socket.send(msg.encode())
                print('Вы вышли из чата')
                raise Exception
            msg_for_send = f'{username}: {msg}'
            socket.send(msg_for_send.encode())
            print(msg_for_send)
        except Exception as e:
            logging.exception(e)
            socket.close()
            break


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((HOST, PORT))
    print(f'Вы подключились к чату {HOST}:{PORT}. Добро пожаловать. Для выхода напишите "quit"')
except Exception as e:
    logging.exception(e)
    print(f'Сервер недоступен')
    sys.exit()

receive_thr = threading.Thread(target=receive)
send_thr = threading.Thread(target=send)

receive_thr.start()
send_thr.start()
