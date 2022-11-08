import socket
from threading import Thread

SOCK_BUFFER = 1024

t_counter = 0

def client_handler(conn, client_address):
    global t_counter

    t_counter += 1
    print(f"Cantidad de hilos en este momento: {t_counter}")

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
    
    t_counter -= 1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        
        t = Thread(target=client_handler, args=(conn, client_address))
        t.start()
