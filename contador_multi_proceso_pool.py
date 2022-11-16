import time
from multiprocessing import Pool

CUENTA = 50_000_000

num_proc = 4


def cuenta(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    inputs = [CUENTA // num_proc] * num_proc
    p = Pool(processes=num_proc)
    
    inicio = time.perf_counter()
    res = p.map(cuenta, inputs)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo transcurrido: {fin - inicio:.2f} segundos")