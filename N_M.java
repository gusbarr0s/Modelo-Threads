import java.util.concurrent.*;

public class N_M {
    public static void main(String[] args) throws Exception {

        int n = 1000; //escolhe a quantidade
        int tempoTrabalhoMs = 10;
        int tamanhoPool = Runtime.getRuntime().availableProcessors(); //threads do meu pc
        System.out.println("modelo N:M");
        System.out.println("threads " + n);
        System.out.println("threads sistema: " + tamanhoPool);
        ExecutorService pool = Executors.newFixedThreadPool(tamanhoPool);
        long inicio = System.nanoTime(); //comeco
        // manda as n tarefas para o pool fixo
        for (int i = 0; i < n; i++) {
            pool.submit(() -> {
                try { Thread.sleep(tempoTrabalhoMs); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            });
        }
        pool.shutdown();
        pool.awaitTermination(1, TimeUnit.MINUTES);
        long fim = System.nanoTime(); //fim
        long tempoTotalMs = (fim - inicio) / 1_000_000;

        System.out.println("Tempo total: " + tempoTotalMs + " ms");
    }
}
