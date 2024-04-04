import java.io.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static int max = 0;
    static int[][] arr = new int[11][11];

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            String[] tmpArr = tmp.split(" ");
            for (int j = 0; j < n; j++)
                arr[i][j] = Integer.parseInt(tmpArr[j]);
        }

        backTracking(0, 0, 0, new boolean[n]);
        System.out.println(max);
    }

    static void backTracking(int x, int y, int sum, boolean[] visited) {
        if (y == n) {
            if (sum > max)
                max = sum;
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i])
                continue;

            visited[i] = true;
            backTracking(i, y + 1, sum + arr[i][y], visited);
            visited[i] = false;
        }
    }
}