import asyncio
import time
import random

async def cuenta(idx):
    sleep_time = random.randint(1, 10)
    print(f"Valor aleatorio de {idx} es {sleep_time}")
    await asyncio.sleep(0.1)
    print(f"Uno de {idx}")
    await asyncio.sleep(sleep_time)
    print(f"Dos de {idx}")


async def main():
    await asyncio.gather(*(cuenta(i) for i in range(3)))



if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin - inicio:.2f} segundos")
