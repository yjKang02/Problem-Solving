import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

num = 0
for i in range(n):
    for j in range(m - 1):
        num += 1
        print(str(num) + ' ')
    num += 1
    print(str(num) + '\n')