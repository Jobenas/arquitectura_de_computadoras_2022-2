import asyncio
import time

from aiohttp import ClientSession

async def fetch_url(url: str, session: ClientSession, **kwargs) -> int:
    try:
        print(f"Fetching {url}")
        resp = await session.request(method="GET", url=url, **kwargs)
        resp.raise_for_status()

        print(f"Status code: {resp.status} de {url}")
        return resp.status
    except Exception as e:
        print(f"Status code: 404 de {url}")
        return 404


async def main():
    with open("urls.txt", "r") as f:
        contenido = f.read()

    urls = contenido.split("\n")

    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(url, session))
        
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
