#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

char** solution(int** line, size_t line_rows, size_t line_cols) {
    long crossPoint[line_rows * (line_rows - 1) / 2][2];
    long crossCnt = 0;
    long minX, maxX, minY, maxY;

    for (int i = 0; i < line_rows; i++) {
        long a = line[i][0];
        long b = line[i][1];
        long e = line[i][2];
        for (int j = i + 1; j < line_rows; j++) {
            long c = line[j][0];
            long d = line[j][1];
            long f = line[j][2];

            long ad_bc = a * d - b * c;

            if (ad_bc == 0) continue;

            double x = (double)(b * f - e * d) / ad_bc;
            double y = (double)(e * c - a * f) / ad_bc;

            if (x == (long)x && y == (long)y) {
                if (!crossCnt) {
                    minX = maxX = x;
                    minY = maxY = y;
                } else {
                    if (x < minX) minX = x;
                    if (x > maxX) maxX = x;
                    if (y < minY) minY = y;
                    if (y > maxY) maxY = y;
                }

                crossPoint[crossCnt][0] = x;
                crossPoint[crossCnt++][1] = y;
            }
        }
    }

    char** answer = (char**)malloc(sizeof(char*) * (maxY - minY + 2));
    for (int i = 0; i < maxY - minY + 1; i++) {
        answer[i] = (char*)malloc(sizeof(char) * (maxX - minX + 2));
        for (int j = 0; j < maxX - minX + 1; j++) answer[i][j] = '.';
        answer[i][maxX - minX + 1] = '\0';
    }

    for (int i = 0; i < crossCnt; i++)
        answer[maxY - crossPoint[i][1]][crossPoint[i][0] - minX] = '*';

    return answer;
}