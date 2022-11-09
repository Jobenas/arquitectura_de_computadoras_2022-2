import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        print(f"Thread {name}: Iniciando la actualizacion")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name}: Actualizacion completa")


if __name__ == "__main__":
    workers = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    print(f"Valor final de la base de datos: {db.value}")
