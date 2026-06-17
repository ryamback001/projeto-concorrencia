import threading
import queue
import os

# Fila compartilhada
fila = queue.Queue()

# Variável compartilhada
total_palavras = 0

# Lock para sincronização
lock = threading.Lock()

# Lista de erros
erros = []

def contar_palavras(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    return len(texto.split())


def worker():
    global total_palavras

    while not fila.empty():

        arquivo = fila.get()

        try:
            qtd = contar_palavras(arquivo)

            with lock:
                total_palavras += qtd

            print(f"{arquivo}: {qtd} palavras")

        except Exception as e:

            with lock:
                erros.append((arquivo, str(e)))

        finally:
            fila.task_done()


def main():

    pasta = "arquivos"

    for nome in os.listdir(pasta):

        if nome.endswith(".txt"):
            fila.put(os.path.join(pasta, nome))

    threads = []

    for _ in range(4):

        t = threading.Thread(target=worker)

        t.start()

        threads.append(t)

    fila.join()

    for t in threads:
        t.join()

    print("\n===== RESULTADO =====")
    print(f"Total de palavras: {total_palavras}")

    if erros:
        print("\nArquivos com erro:")
        for erro in erros:
            print(erro)


if __name__ == "__main__":
    main()