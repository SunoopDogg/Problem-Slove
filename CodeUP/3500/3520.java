import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static int cnt = 0;
    static int printCnt = 3;
    static int[] arr = new int[13];

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        backTracking(0);

        System.out.println(cnt);
    }

    static void backTracking(int x) {
        if (x == n) {
            cnt++;
            if (printCnt-- > 0) {
                for (int i = 0; i < n; i++)
                    System.out.print((arr[i] + 1) + " ");
                System.out.println();
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            arr[x] = i;
            if (check(x))
                backTracking(x + 1);
        }
    }

    static boolean check(int index) {
        for (int i = 0; i < index; i++)
            if (arr[i] == arr[index] || Math.abs(arr[i] - arr[index]) == index - i)
                return false;
        return true;
    }
}