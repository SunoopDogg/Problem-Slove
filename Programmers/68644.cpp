#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int* solution(int numbers[], size_t numbers_len) {
    int arr[201] = {0};
    int list[201] = {0};
    int cnt = 0;

    for (size_t i = 0; i < numbers_len; i++)
        for (size_t j = 0; j < numbers_len; j++) {
            if (i == j || list[numbers[i] + numbers[j]] == 1) continue;
            arr[cnt++] = numbers[i] + numbers[j];
            list[numbers[i] + numbers[j]] = 1;
        }

    int* answer = (int*)malloc(sizeof(int) * cnt);

    for (int i = 0; i < cnt; i++)
        for (int j = 0; j < cnt - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }

    for (int i = 0; i < cnt; i++) answer[i] = arr[i];

    return answer;
}