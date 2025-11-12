import sys
input = sys.stdin.readline

isbn = list(input())

check = 0
index = 0

for i in range(13):
    if isbn[i] != '*':
        check += (int(isbn[i]) * (1 if (i % 2 == 0) else 3))
    else:
        index = i
        
print(check * (9 if index % 2 == 0 else 3) % 10)