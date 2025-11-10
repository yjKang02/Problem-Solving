'''
문제 링크 : https://www.acmicpc.net/problem/11660
문제 제목 : 구간 합 구하기 5
solved.ac 티어 : 실버 1
알고리즘 분류 :
다이나믹 프로그래밍
누적 합
'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]
matrix = [list(map(int, input().split())) for _ in range(n)]

sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + matrix[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]
    print(str(answer)+'\n')


