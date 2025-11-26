n = int(input())

def GCD(a: int, b: int):
    r = a % b
    if r != 0:
        return GCD(b, r)
    else:
        return b

for _ in range(n):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    lcm = a * b // gcd
    print(lcm, gcd)
