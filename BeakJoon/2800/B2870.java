import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class B2870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<BigInteger> num = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] temp = br.readLine().split("\\D");

            for (int j = 0; j < temp.length; j++)
                if (temp[j] != "")
                    num.add(new BigInteger(temp[j]));
        }

        num.sort(null);

        for (int i = 0; i < num.size(); i++)
            System.out.println(num.get(i));
    }
}