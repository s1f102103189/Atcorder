N, S, K = map(int, input().split())
P = [list(map(int, input().split())) for i in range(N)]

result = 0
for i in range(N):
    result += P[i][0] * P[i][1]
if result < S:
    print(result + K)
else:
    print(result)
