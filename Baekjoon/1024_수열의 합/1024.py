import sys
input = sys.stdin.readline
print = sys.stdout.write

# 리스트의 최소 길이가 l
n, l = map(int, input().split())
answer = -1
for i in range(l, 101):
    la = (2 * n) - (i * (i - 1))
    if la % (2 * i) == 0 and la // (2 * i) >= 0:
        answer = la // (2 * i)
        for i in range(i - 1):
            print(str(answer) + ' ')
            answer += 1
        print(str(answer))
        break

if answer == - 1: print(str(answer))