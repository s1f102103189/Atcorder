# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# result = []

# for i in range(n):
#     for t in range(matrix):
#         if matrix[t][i] == 1:
#             result.append(t+1)
#             print(result)

# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             print(f"{j+1}")

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result = []
    for t in range(n):
        if matrix[i][t] == 1:
            result.append(t+1)
    if result:
        print(" ".join(map(str, result)))