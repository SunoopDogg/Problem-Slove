import java.io.*;

public class B1309 {
    static int memo[] = new int[100001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        System.out.println(dynamicProgram(n));
    }

    static int dynamicProgram(int n) {
        if (n < 2)
            return n == 0 ? 1 : 3;
        if (memo[n] != 0)
            return memo[n];
        return memo[n] = (dynamicProgram(n - 1) * 2 + dynamicProgram(n - 2)) % 9901;
    }
}