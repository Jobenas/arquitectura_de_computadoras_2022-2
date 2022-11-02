import time

def cuenta():
    print("Uno")
    time.sleep(1)
    print("Dos")

def main():
    for _ in range(3):
        cuenta()


if  __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin - inicio:.2f} segundos")

