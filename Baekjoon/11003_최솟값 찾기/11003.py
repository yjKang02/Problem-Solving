import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write
n, l = map(int, input().split())

a = list(map(int, input().split()))

# # 시간초과
# queue = []
# for i in range(n):
#     queue.append(a.pop(0))
#     if i + 1 > l:
#         queue.pop(0)
#     print(str(min(queue)) + ' ')

deq = deque([a.pop])

for i in range(1, n):
    deq.append(a.pop)
    