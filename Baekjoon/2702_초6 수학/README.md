# [Bronze 2] 2702_초6 수학

[문제 링크](https://www.acmicpc.net/problem/2702) 

### 🛠️ 분류
수학, 브루트포스 알고리즘, 정수론, 사칙연산

### 💡 접근 방법
a와 b의 최대공약수(GCD, Greatest Common Divisor), 최소공배수(LCM, Least Common Multiple)를 구하는 문제.

유클리드 호제법을 이해한다면 쉽게 풀 수 있는 문제다.
#### 유클리드 호제법
- 최소공약수를 구하는 알고리즘
- 두 수 $a$와 $b$가 있을 때 $(a > b)$, $a$를 $b$로 나눌 경우, $a = bq + r$ ($q$는 몫, $r$은 나머지)
- 이 때, $a$와 $b$의 최대공약수는, $b$와 $r$의 최대공약수와 같다.

그러므로 a를 a/b의 나머지 r로 다시 b를 나누어 이 과정을 반복한 후, 나머지가 0이 된 경우, 나눈 값이 두 값의 최소공약수가 됩니다.

최소공배수는 a * b / 최소공약수이므로 쉽게 구할 수 있다.

### 🗝️ Key Code (핵심 코드)
```python
def GCD(a: int, b: int):
    r = a % b
    if r != 0:
        return GCD(b, r)
    else:
        return b
```
```python
lcm = a * b // gcd