package Programmers;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";

        int lastLeftHandPosition = 10;
        int lastRightHandPosition = 12;

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] += numbers[i] == 0 ? 11 : 0;

            switch ((numbers[i] + 2) % 3) {
                // 좌측 키패드
                case 0:
                    answer += 'L';
                    lastLeftHandPosition = numbers[i];
                    break;
                // 우측 키패트
                case 2:
                    answer += 'R';
                    lastRightHandPosition = numbers[i];
                    break;
                // 중앙 키패트
                case 1:
                    int leftRowDistance = Math.abs((numbers[i] + 2) % 3 - (lastLeftHandPosition - 1) % 3);
                    int leftColumnDistance = Math.abs((numbers[i] - 1) / 3 - (lastLeftHandPosition - 1) / 3);
                    Float leftHandDistance = leftRowDistance + leftColumnDistance
                            + (float) (hand.startsWith("l") ? -0.5 : +0.5);
                    int rightRowDistance = Math.abs((numbers[i] + 2) % 3 - (lastRightHandPosition - 1) % 3);
                    int rightColumnDistance = Math.abs((numbers[i] - 1) / 3 - (lastRightHandPosition - 1) / 3);
                    Float rightHandDistance = (float) (rightRowDistance + rightColumnDistance);

                    if (leftHandDistance < rightHandDistance) {
                        answer += 'L';
                        lastLeftHandPosition = numbers[i];
                    } else {
                        answer += 'R';
                        lastRightHandPosition = numbers[i];
                    }
                    System.out.println(lastLeftHandPosition + " " + lastRightHandPosition + " " + numbers[i] + " "
                            + leftHandDistance + " " + rightHandDistance + " ");
                    break;
            }
        }

        return answer;
    }
}