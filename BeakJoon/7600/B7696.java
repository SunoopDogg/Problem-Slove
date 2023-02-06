import java.util.Scanner;

public class B7696 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        int[] memo = new int[1000001];

        while (true) {
            int n = sc.nextInt();

            if (n == 0)
                break;

            if (memo[n] != 0) {
                System.out.println(memo[n]);
                continue;
            }

            int cnt = 0;
            for (int i = 1;; i++) {
                for (int j = 0; j < 10; j++) {
                    arr[j] = 0;
                }

                int temp = i;
                int flag = 1;
                while (temp > 0) {
                    if (++arr[temp % 10] > 1) {
                        flag = 0;
                        break;
                    }
                    temp /= 10;
                }

                if (flag == 1) {
                    cnt++;
                    memo[cnt] = i;
                    if (cnt == n) {
                        System.out.println(i);
                        break;
                    }
                }
            }
        }
    }
}