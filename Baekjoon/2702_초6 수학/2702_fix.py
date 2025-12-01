n = int(input())

# 안전을 위해 재귀함수에서 while문으로 변경
def GCD(a: int, b: int):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a: int, b: int, gcd: int):
    return a * b // gcd

for _ in range(n):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    lcm = LCM(a, b, gcd)
    print(lcm, gcd)
