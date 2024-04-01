import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[10];

        for (int i = a; i <= b; i++) {
            int tmp = i;
            while (tmp > 0) {
                arr[tmp % 10]++;
                tmp /= 10;
            }
        }

        if (a == 0 && b == 0 && k == 0)
            System.out.println(1);
        else
            System.out.println(arr[k]);
    }
}