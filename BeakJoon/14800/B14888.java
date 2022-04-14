import java.io.*;

public class B14888 {
    static int n;
    static int operands[] = new int[12];
    static int operators[] = new int[5];
    static int max = -1000000001;
    static int min = 1000000001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        String tmp = br.readLine();
        String[] tmpArr = tmp.split(" ");
        for (int i = 0; i < n; i++)
            operands[i] = Integer.parseInt(tmpArr[i]);

        tmp = br.readLine();
        tmpArr = tmp.split(" ");
        for (int i = 0; i < 4; i++)
            operators[i] = Integer.parseInt(tmpArr[i]);

        backTrack(1, operands[0]);

        System.out.println(max);
        System.out.println(min);
    }

    static void backTrack(int idx, int result) {
        if (idx == n) {
            if (result > max)
                max = result;
            if (result < min)
                min = result;
            return;
        }

        for (int i = 0; i < 4; i++)
            if (operators[i] > 0) {
                operators[i]--;

                if (i == 0)
                    backTrack(idx + 1, result + operands[idx]);
                else if (i == 1)
                    backTrack(idx + 1, result - operands[idx]);
                else if (i == 2)
                    backTrack(idx + 1, result * operands[idx]);
                else
                    backTrack(idx + 1, result / operands[idx]);

                operators[i]++;
            }
    }
}