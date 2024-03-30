N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

def calculate_missing_sum(N, K, A):
    total_sum = 0
    for i in range(1, K + 1):
        if i not in A:
            total_sum += i
    return total_sum

# 入力例 1
print(calculate_missing_sum(N, K, A))
