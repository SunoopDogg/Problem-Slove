import java.util.Scanner;

public class B1264 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str;

        while (true) {
            int cnt = 0;
            str = sc.nextLine();

            if (str.equals("#"))
                break;

            str = str.toLowerCase();
            for (int i = 0; i < str.length(); i++) {
                switch (str.charAt(i)) {
                    case 'a':
                    case 'e':
                    case 'i':
                    case 'o':
                    case 'u':
                        cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
}