N = int(input())
M = list(map(int, input().split()))
result = 0

for i in range(N):
    result += M[i]
    if result < 0:
        result = 0

print(result)