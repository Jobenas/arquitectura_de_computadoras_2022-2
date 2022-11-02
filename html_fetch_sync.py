import requests
import time

def fetch_url(url: str) -> int:
    print(f"Fetching {url}")
    resp = requests.get(url)
    print(f"Status code: {resp.status_code} de {url}")
    return resp.status_code

def main():
    with open("urls.txt", "r") as f:
        contenido = f.read()
    
    urls = contenido.split("\n")

    for url in urls:
        status_code = fetch_url(url)


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")