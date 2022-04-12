import java.io.*;

public class B9342 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            int startA = str.indexOf("A");
            int startF = str.indexOf("F");
            int startC = str.indexOf("C");

            if (str.charAt(0) <= 'F' && str.charAt(str.length() - 1) <= 'F')
                if (startA < startF && startF < startC)
                    if (str.charAt(startF - 1) == 'A' && str.charAt(startC - 1) == 'F') {
                        System.out.println("Infected!");
                        continue;
                    }
            System.out.println("Good");
        }
    }
}