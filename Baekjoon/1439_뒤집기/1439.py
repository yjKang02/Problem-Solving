import sys
input = sys.stdin.readline

string = [i == '1' for i in input()]
string.pop(-1)
key = string.pop(0)

count = 0

for i in string:
    if i != key:
        count += 1
        key = i

print((count // 2) + (count % 2))