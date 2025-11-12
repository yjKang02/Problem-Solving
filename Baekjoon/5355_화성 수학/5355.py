t = int(input())
for _ in range(t):
    li = input().split()
    answer = float(li[0])
    for i in range(1, len(li)):
        if li[i] == '@':
            answer *= 3
        elif li[i] == '%':
            answer += 5
        elif li[i] == '#':
            answer -= 7
    
    print(f"{answer:.2f}")