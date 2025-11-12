import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

answer_t = 0
for i in range(6):
    answer_t += ((size[i] + t - 1) // t)

print(answer_t)
print(n // p, n % p)