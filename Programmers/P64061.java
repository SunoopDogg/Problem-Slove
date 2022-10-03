package Programmers;

import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> basket = new ArrayList<>();

        for (int i = 0; i < moves.length; i++) {
            for (int j = 0; j < board.length; j++)
                if (board[j][moves[i] - 1] > 0) {
                    basket.add(board[j][moves[i] - 1]);
                    board[j][moves[i] - 1] = 0;
                    break;
                }

            if (basket.size() > 1)
                if (basket.get(basket.size() - 1) == basket.get(basket.size() - 2)) {
                    basket.remove(basket.size() - 1);
                    basket.remove(basket.size() - 1);
                    answer += 2;
                }
        }

        return answer;
    }
}