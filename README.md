# Modelo-Threads
rodei cada um pelo menos 5x pra ter mais precisao

tava curioso e fiz um modelinho em Pyhton tambem, usando as bibliotecas concurrent.futures(NM) e threading(1:1)

em Python pro tamanho da Pool eu nao consegui o equivalente ao Runtime.getRuntime().availableProcessors(); do java

entao acabou que eu so deixei a variavel responsavel pelo tamanho da pool setada pra 16, que sao quantas threads eu tenho no meu computador

OS RESULTADOS DOS TESTES ABAIXO SAO DA EXECUCAO DO PROGRAMA EM JAVA

1:1 threads : 10 - 13ms(em todas)

1:1 threads : 100 - 18ms(min)/21(max)  

1:1 threads : 500 - 41ms(min)/48ms(max)

1:1 threads : 1000 - 72ms(min)/81ms(max)

considerando que tenho 16 threads no sistema:

NM threads : 10 - 12ms(min)/16ms(max)

NM threads : 100 - 75ms(em todas)

NM threads : 500 - 337ms(min)/341(max)

NM threads : 1000 - 665(min)671ms(max)

Conclusao final:  nesta situacao o 1:1 parece mais vantajoso que o NM

ele desempenha muito melhor que o NM em praticamente todos os resultados, so quando o numero de threads é pequeno que os resultados sao proximos

eu acredito que o resultado seja um pouco "enganoso" ja que na teoria o NM seria superior ao 1:1 em questao de desempenho

eu acho que isso acontece devido ao fato da tarefas escolhidas sao curtas e leves, tornando o custo de gerenciamento do ExecutorService relativamente alto se comparado com a criacao direta de threads reais

neste contexto o modelo 1:1 obteve tempos menores e mais consistentes, oque comprova que o desempenho pode variar dependendo do tipo de tarefa e da capacidade do hardware



