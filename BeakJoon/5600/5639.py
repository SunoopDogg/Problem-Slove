import sys
sys.setrecursionlimit(10**9)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


def solution(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    solution(s+1, mid-1)
    solution(mid, e)
    print(nums[s])


solution(0, len(nums)-1)
