import time
import concurrent.futures

def main():
    n = 1000 #tem que escolher aqui tb
    tempo_trabalho = 0.01 
    tamanho_pool = 16 #sao quantas threads eu tenho no meu pc mesmo

    print("modelo N:M ")
    print("threads:", n)
    print("threads sistema", tamanho_pool)

    inicio = time.time()#comeco
    
    #cria um pool fixo de threads reais
    with concurrent.futures.ThreadPoolExecutor(max_workers=tamanho_pool) as executor:
        for _ in range(n):
            executor.submit(time.sleep, tempo_trabalho)

    fim = time.time()  #fim
    tempo_total_ms = (fim - inicio) * 1000 #ms
    print("tempo total: ", tempo_total_ms,"ms")

if __name__ == "__main__":
    main()

