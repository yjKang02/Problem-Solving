n, x, y = map(int, input().split())

i = 1
def tournament(a: int):
    return (a + 1) // 2

while True:
    x = tournament(x)
    y = tournament(y)
    if x == y:
        break
    i += 1
print(i)