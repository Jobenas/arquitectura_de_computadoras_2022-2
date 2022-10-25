import time

labs = []
nl = 0


def calcula_nota(labs, ta):
    for lab in labs:
        nl += lab
    nl /= len(labs)

    nota_final = ((nl * 7) + (ta * 3)) / 10

    return nota_final

if __name__ == "__main__":
    inicio_global = time.perf_counter()
    inicio_captura = time.perf_counter()

    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    fin_captura = time.perf_counter()

    inicio_cpu = time.perf_counter()

    filas = contenido.split("\n")
    cabecera = filas[0]
    filas = filas[1:]

    for fila in filas:
        cols = fila.split(",")
        for i in range(1, 11):
            labs.append(float(cols[i]))

        ta = float(cols[11])

        for lab in labs:
            nl += lab
        nl /= len(labs)

        nota_final = ((nl * 7) + (ta * 3)) / 10

        print(f"La nota final es: {nota_final}")

    fin_cpu = time.perf_counter()
    fin_global = time.perf_counter()

    print(f"Tiempo de captura: {fin_captura - inicio_captura} segundos")
    print(f"Tiempo de CPU: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo global: {fin_global - inicio_global} segundos")
    print(f"estadisticas: porcentaje de captura: {(fin_captura - inicio_captura) / (fin_global - inicio_global) * 100}%, porcentaje de cpu: {(fin_cpu - inicio_cpu) / (fin_global - inicio_global) * 100}%")
