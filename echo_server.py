import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    # crea el objeto de socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    # asociamos la direccion y puerto al objeto socket
    sock.bind(server_address)

    # iniciamos la escucha de conexiones
    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)
                if data:
                    # print(f"Recibido: {data.decode('utf-8')}")
                    print(f"Recibido: {data}")
                    conn.sendall(data)
                else:
                    print("No hay mas datos")
                    break
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
