public class M1_1 {
    public static void main(String[] args) throws Exception {

        int n = 1000; //escolhe a quantidade
        int tempoTrabalhoMs = 10;

        System.out.println("modelo 1:1");
        System.out.println("threads: " + n);
        Thread[] threads = new Thread[n];
        long inicio = System.nanoTime(); //começo
        //cria e inicia as threads
        for (int i = 0; i < n; i++) {
            threads[i] = new Thread(() -> {
                try { Thread.sleep(tempoTrabalhoMs); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            });
            threads[i].start();
        }
        for (int i = 0; i < n; i++) threads[i].join();
        long fim = System.nanoTime(); //
        long tempoTotalMs = (fim - inicio) / 1_000_000;

        System.out.println("Tempo total: " + tempoTotalMs + " ms");
    }
}
