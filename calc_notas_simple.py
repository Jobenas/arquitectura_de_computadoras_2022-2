import time

labs = []
ta = 0
nl = 0

if __name__ == "__main__":
    inicio_global = time.perf_counter()
    inicio_captura = time.perf_counter()

    for i in range(10):
        nota = input(f"Ingrese la nota del laboratorio {i+1}: ")
        labs.append(int(nota))

    ta = int(input("Ingrese la nota de la tarea academica: "))

    fin_captura = time.perf_counter()

    inicio_cpu = time.perf_counter()

    for lab in labs:
        nl += lab
    nl /= len(labs)

    nota_final = ((nl * 7) + (ta * 3)) / 10

    fin_cpu = time.perf_counter()
    fin_global = time.perf_counter()

    print(f"La nota final es: {nota_final}")
    print(f"Tiempo de captura: {fin_captura - inicio_captura} segundos")
    print(f"Tiempo de CPU: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo global: {fin_global - inicio_global} segundos")
    print(f"estadisticas: porcentaje de captura: {(fin_captura - inicio_captura) / (fin_global - inicio_global) * 100}%, porcentaje de cpu: {(fin_cpu - inicio_cpu) / (fin_global - inicio_global) * 100}%")

