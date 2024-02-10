# A = list(map(int, input().split()))

# if len(A) < 3:
#     print("Error")
# else:
#     result = []
#     result.append(A[0])
#     n = A[0] + A[2]
#     while True:
#         result.append(n)
#         n += A[2]
#         if n == A[1]:
#             break
#     result2 = ' '.join(str(res) for res in result)
#     print(result2)

A = list(map(int, input().split()))

result = range(A[0], A[1]+1, A[2])
result2 = list(result)
result3 = ' '.join(str(res) for res in result2)
print(result3)