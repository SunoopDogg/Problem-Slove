import java.io.*;
import java.util.*;

public class B14891 {
    static List<List<Integer>> gear = new ArrayList<>();
    static int rotation[] = new int[4];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 4; i++) {
            String tmp = br.readLine();
            String[] tmpArr = tmp.split("");
            gear.add(new ArrayList<>());
            for (int j = 0; j < 8; j++)
                gear.get(i).add(Integer.parseInt(tmpArr[j]));
        }

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            String[] tmpArr = tmp.split(" ");
            int g = Integer.parseInt(tmpArr[0]);
            int r = Integer.parseInt(tmpArr[1]);

            setRotation(new boolean[4], g - 1, r);

            for (int j = 0; j < 4; j++)
                rotate(j);
        }

        System.out.println(getScore());
    }

    static void setRotation(boolean[] check, int g, int r) {
        if (g < 0 || g > 3)
            return;
        if (check[g])
            return;

        check[g] = true;
        rotation[g] = r;

        setRotation(check, g - 1, r * isSameTeeth(g, g - 1, 6, 2));
        setRotation(check, g + 1, r * isSameTeeth(g, g + 1, 2, 6));
    }

    static int isSameTeeth(int x, int y, int a, int b) {
        if (x < 0 || x > 3 || y < 0 || y > 3)
            return 0;

        if (gear.get(x).get(a) != gear.get(y).get(b))
            return -1;
        else
            return 0;
    }

    static void rotate(int n) {
        if (rotation[n] == 1) {
            gear.get(n).add(0, gear.get(n).remove(7));
        } else if (rotation[n] == -1)
            gear.get(n).add(gear.get(n).remove(0));
    }

    static int getScore() {
        int result = 0;

        for (int i = 0; i < 4; i++)
            if (gear.get(i).get(0) == 1)
                result += Math.pow(2, i);

        return result;
    }
}