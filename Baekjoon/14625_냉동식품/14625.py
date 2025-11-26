start = list(map(int, input().split()))
end = list(map(int, input().split()))
n = int(input())

answer = 0

while(True):
    if(start[0] // 10 == n or start[0] % 10 == n
       or start[1] // 10 == n or start[1] % 10 == n):
        answer += 1
        
    if start[0] == end[0] and start[1] == end[1]:
        break
        
    start[1] += 1
    
    if(start[1] >= 60):
        start[1] = 0
        start[0] += 1
    if(start[0] >= 24):
        start[0] = 0
        
print(answer)