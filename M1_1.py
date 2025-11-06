import time
import threading

def main():
    n = 10  #escolhe aqui tb
    tempo_trabalho = 0.01
  
    print("modelo 1:1")
    print("threads reais", n)
    threads = []
    inicio = time.time()#comeco
    #cria e inicia todas as threads reais
    for _ in range(n):
        t = threading.Thread(target=time.sleep, args=(tempo_trabalho,))
        threads.append(t)
        t.start()
    #espera todas terminarem
    for t in threads:
        t.join()

    fim = time.time()  #fim
    tempo_total_ms = (fim - inicio) * 1000
    print("tempo total: ", tempo_total_ms,"ms")

if __name__ == "__main__":
    main()
