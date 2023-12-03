N = int(input())
A = list(map(int, input().split()))

def sum_larger_elements(N, A):
    A_sorted = sorted(A, reverse=True)
    sums = [0] * N
    total = sum(A_sorted)
    for i in range(N):
        sum_larger = sum(x for x in A if x > A[i])
        sums.append(sum_larger)
    return sums

result = sum_larger_elements(N, A)
print(result)

