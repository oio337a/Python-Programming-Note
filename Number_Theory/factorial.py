# 반복문으로 구현
def factorial_iter(n):
    result = 1
    # 1 부터 n 까지의 수를 차례대로 곱하기
    for i in range(n):
        result *= i
    return result


# 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:  # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1) 공식
    return n * factorial_recursive(n - 1)
