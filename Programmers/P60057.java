package Programmers;

class Solution {
    public int solution(String s) {
        String shortCompression = s;

        for (int i = 1; i <= s.length(); i++) {
            String target;
            int targetCount;
            String compression = "";

            for (int j = 0; j < s.length(); j += i) {

                target = GetTargetString(s, j, i);
                if (target == null) {
                    compression += s.substring(j, s.length());
                    break;
                }

                targetCount = GetTargetCount(s, target, j);
                if (targetCount <= 0)
                    break;

                compression += CreateCompressedString(target, targetCount);

                j += targetCount * i - i;
            }

            if (shortCompression.length() > compression.length())
                shortCompression = compression;
        }

        return shortCompression.length();
    }

    static String GetTargetString(String str, int index, int length) {
        String result = "";

        if (str.length() < index + length)
            return null;

        for (int i = index; i < index + length; i++)
            result += str.charAt(i);

        return result;
    }

    static int GetTargetCount(String str, String target, int index) {
        int result = 0;

        if (str.length() < index + target.length())
            return -1;

        for (int i = index; i <= str.length() - target.length(); i += target.length())
            if (target.equals(str.substring(i, i + target.length())))
                result++;
            else
                break;

        return result;
    }

    static String CreateCompressedString(String target, int targetCount) {
        String result = "";

        if (targetCount > 1)
            result += String.valueOf(targetCount);
        result += target;

        return result;
    }
}