import matplotlib.pyplot as plt

threads = [10, 100, 500, 1000]
modelo_11 = [13, 20, 45, 76]
modelo_nm = [14, 75, 339, 668]

plt.figure(figsize=(8, 4))
plt.plot(threads, modelo_11, marker='o', label='Modelo 1:1', color='red')
plt.plot(threads, modelo_nm, marker='o', label='Modelo N:M', color='black')#aqui é furacao kkkkk
plt.title('desempenho comparativo 1:1 e N:M')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo Total (ms)')
plt.legend()
plt.xticks(threads)

plt.show()
