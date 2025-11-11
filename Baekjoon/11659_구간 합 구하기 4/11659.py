import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

li = [0] * n
li = list(map(int, input().split()))

sum = [0] * (n + 1)
for i in range(1, n + 1):
    sum[i] = li[i - 1] + sum[i - 1] 

for i in range(m):
    x1 , x2 = map(int, input().split())
    print(str(sum[x2] - sum[x1 - 1]) + "\n")

