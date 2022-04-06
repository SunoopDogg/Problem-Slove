import java.io.*;
import java.util.*;

public class B2457 {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int arr[][] = new int[n][2];

        for (int i = 0; i < n; i++) {
            String tmp[] = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(tmp[0]) * 100 + Integer.parseInt(tmp[1]);
            arr[i][1] = Integer.parseInt(tmp[2]) * 100 + Integer.parseInt(tmp[3]);
        }

        Arrays.sort(arr, (o1, o2) -> {
            return o1[0] != o2[0] ? o1[0] - o2[0] : o2[1] - o1[1];
        });

        System.out.println(greedy(arr, 0, 301, 0));
    }

    static int greedy(int arr[][], int cnt, int end, int idx) {
        if (end > 1130)
            return cnt;

        if (idx >= n)
            return 0;

        if (arr[idx][0] > end)
            return 0;

        int newEnd = end;

        for (int i = idx; i < n; i++) {
            if (arr[i][0] > end)
                break;
            if (arr[i][1] > newEnd) {
                newEnd = arr[i][1];
                idx++;
            }
        }

        return greedy(arr, cnt + 1, newEnd, idx);
    }
}