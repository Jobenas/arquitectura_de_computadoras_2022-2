import time
import concurrent.futures
from threading import Lock


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()


    def update(self, name):
        print(f"Thread {name} iniciando actualizacion")
        print(f"Thread {name} a punto de adquirir el candado")
        with self._lock:
            print(f"Thread {name} ha adquirido el candado")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name} a punto de liberar el candado")
        print(f"Thread {name} ha liberado el candado")
        print(f"Thread {name} ha terminado la actualizacion")


if __name__ == "__main__":
    workers = 5
    tareas = workers * 2
    db = FakeDatabase()
    print(f"El valor inicial de la base de datos es {db.value}")
    inicio = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(tareas):
            executor.submit(db.update, index)
    fin = time.perf_counter()
    print(f"El valor final de la base de datos es {db.value}")
    print(f"Tiempo total: {fin - inicio} segundos")

