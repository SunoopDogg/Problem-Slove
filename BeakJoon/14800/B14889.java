import java.io.*;

public class B14889 {
    static int n;
    static int arr[][] = new int[21][21];
    static boolean check[] = new boolean[21];
    static int min = 1000000001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            String[] tmpArr = tmp.split(" ");
            for (int j = 0; j < n; j++)
                arr[i][j] = Integer.parseInt(tmpArr[j]);
        }

        backTracking(0, 0);
        System.out.println(min);
    }

    static void backTracking(int idx, int cnt) {
        if (cnt == n / 2) {
            int result1 = 0;
            int result2 = 0;

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (i == j)
                        continue;
                    else if (check[i] && check[j])
                        result1 += arr[i][j];
                    else if (!check[i] && !check[j])
                        result2 += arr[i][j];

            min = Math.min(min, Math.abs(result1 - result2));

            if (min == 0) {
                System.out.println(min);
                System.exit(0);
            }
            return;
        }

        for (int i = idx; i < n; i++) {
            check[i] = true;
            backTracking(i + 1, cnt + 1);
            check[i] = false;
        }
    }
}