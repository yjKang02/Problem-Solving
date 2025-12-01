# [Bronze I] 23881_알고리즘 수업 - 선택 정렬 2

[문제 링크](https://www.acmicpc.net/problem/23881) 

### 🛠️ 분류
구현, 정렬, 시뮬레이션

### 💡 접근 방법
선택 정렬을 직접 구현하면서, 교환이 되는 부분을 카운트 및 출력하면 된다.
구현은 문제에 나와있는 의사 코드를 참조하여 해결하였다.

### 🗝️ Key Code (핵심 코드)
```python
def tournament(a: int):
    return (a + 1) // 2