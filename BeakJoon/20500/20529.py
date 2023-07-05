import sys


def solution(mbti1, mbti2):
    return sum([1 if mbti1[i] != mbti2[i] else 0 for i in range(4)])


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    mbti = sys.stdin.readline().split()

    if N > 16*2:
        print(0)
        continue

    dist = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                dist.append(solution(mbti[i], mbti[j]) +
                            solution(mbti[j], mbti[k]) +
                            solution(mbti[k], mbti[i]))

    print(min(dist))
