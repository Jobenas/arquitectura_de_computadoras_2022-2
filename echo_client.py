import socket
import time

MSG_NUM = 10
SOCK_BUFFER = 4

SLEEP_TIME = 2 # medido en segundos

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        for i in range(MSG_NUM):
            msg = f"Este es el mensaje de prueba {i + 1}"
            msg = msg.encode('utf-8')
            sock.sendall(msg)
            amnt_rcvd = 0
            amnt_exp = len(msg)
            msg_total_bytes = b''

            while amnt_rcvd < amnt_exp:
                data = sock.recv(SOCK_BUFFER)
                print(f"Recibido: {data}")
                amnt_rcvd += len(data)
                msg_total_bytes += data
            print(f"Mensaje total recibido: {msg_total_bytes.decode('utf-8')}")
            time.sleep(SLEEP_TIME)
    finally:
        print("Cerrando socket")
        sock.close()