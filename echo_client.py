import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.25', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        msg = f"Este es el mensaje que se va a enviar al servidor con un buffer de {SOCK_BUFFER} bytes"
        msg = msg.encode('utf-8')
        sock.sendall(msg)

        data = sock.recv(SOCK_BUFFER)
        print(f"Recibido: {data.decode('utf-8')}")
    finally:
        print("Cerrando socket")
        sock.close()