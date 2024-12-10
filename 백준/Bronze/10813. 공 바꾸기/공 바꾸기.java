import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            arr[i] = i;
        }

        int t = 0;
        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            t = arr[a];
            arr[a] = arr[b];
            arr[b] = t;
        }

        for (int i = 1; i < N+1; i++) {
            System.out.printf("%d ", arr[i]);
        }
    }
}
