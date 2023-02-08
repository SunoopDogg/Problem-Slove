import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())

    max_heap = []
    min_heap = []
    valid = {}
    cnt = 0

    for _ in range(k):
        cmd, num = sys.stdin.readline().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(max_heap, (-num, cnt))
            heapq.heappush(min_heap, (num, cnt))

            if num in valid:
                valid[num] += 1
            else:
                valid[num] = 1

            cnt += 1
        else:
            if num == 1:
                while max_heap and valid[-max_heap[0][0]] == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    valid[-max_heap[0][0]] -= 1
                    heapq.heappop(max_heap)
                    cnt -= 1
            else:
                while min_heap and valid[min_heap[0][0]] == 0:
                    heapq.heappop(min_heap)

                if min_heap:
                    valid[min_heap[0][0]] -= 1
                    heapq.heappop(min_heap)
                    cnt -= 1

    if cnt == 0:
        print('EMPTY')
    else:
        while max_heap and valid[-max_heap[0][0]] == 0:
            heapq.heappop(max_heap)

        while min_heap and valid[min_heap[0][0]] == 0:
            heapq.heappop(min_heap)

        print(-max_heap[0][0], min_heap[0][0])
