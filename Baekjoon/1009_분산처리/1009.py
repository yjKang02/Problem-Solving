import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    # answer = pow(a, b, 10)
    # 모듈러 거듭제곱을 이용한 계산
    answer = 1
    while b > 0:
        if b % 2 != 0:
            answer = (answer * a) % 10
        a = (a * a) % 10
        b //= 2
    if answer == 0:
        answer = 10
    print(str(answer) + '\n')