N = int(input())
M = int(input())
button = set()
if M > 0:
    button = set(map(int, input().split()))


def check(n):
    for i in str(n):
        if int(i) in button:
            return False
    return True


def solve():
    if N == 100:
        return 0
    if check(N):
        return min(abs(N-100), len(str(N)))
    answer = abs(N-100)
    for i in range(1000001):
        if check(i):
            answer = min(answer, len(str(i)) + abs(i-N))
    return answer


print(solve())
